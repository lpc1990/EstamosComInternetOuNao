# comando para converter arquivos UI criados pelo UI Designer para um arquivo .py:
# pyside2-uic arquivo.ui -o ui_arquivo.py (ui_arquivo.py - esse ui é somente uma referência
# de nome pra indicar a origem  do arquivo, dizendo que esse arquivo .py foi convertido de um arquivo .ui)

from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction
from ui_janela_principal import Ui_MainWindow
import socket, time, pygame, subprocess, sys, os

# Pega o diretório atual da execução do arquivo atual e joga o path dele na variável diretorio_atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
print("Diretório atual:", diretorio_atual)

# Classe que trabalha com Thread, que é a execução de funções sem travar o programa. Se quiser que uma função seja
# executada sem travar o sistema, deve-se criar uma isntância dessa classe para rodar a função.
class NossaThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.func = None

    def __del__(self):
        self.wait()

    def set_function(self, func, param=None):
        self.func = func
        self.param = param

    def run(self):
        if self.param == None:
            # print("Sem parâmetro!")
            if self.func:
                self.func()
        else:
            if self.func:
                # print("Com parâmetro!")
                self.func(self.param)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadê minha internet?")
        self.setWindowIcon(QIcon(diretorio_atual + "\images\icon.png"))
        self.setFixedSize(412, 698)
        self.busca_informacoes_rede()
        self.definindo_sons()
        self.chamada_da_NossaThread()

        # Aqui começa uma série de comandos para o programa ficar no Tray do windows
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(diretorio_atual + "\images\icon.png"))

        self.tray_menu = QMenu()
        self.show_action = QAction("Abrir", self)
        self.quit_action = QAction("Sair", self)

        self.show_action.triggered.connect(self.show_or_restore_window)
        self.quit_action.triggered.connect(self.quit_application)

        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_activated)
        self.tray_icon.show()

    def show_or_restore_window(self):
        if self.isMinimized() or not self.isVisible():
            self.showNormal()
            self.activateWindow()
        else:
            self.hide()

    def quit_application(self):
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.show()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_or_restore_window()

    def show_window(self):
        self.show()
    # Aqui termina a série de comandos do Tray

    # Seta os sons para cada tipo de aviso do programa
    def definindo_sons(self):
        # inicia a entrada de sons no programa
        pygame.mixer.init()
        self.sons = pygame.mixer.Channel(7)
        self.sons.set_volume(2.0)

        self.som_internet_ok = pygame.mixer.Sound(diretorio_atual + "\sounds\internet_ok_1.mp3")
        self.som_internet_sem_internet = pygame.mixer.Sound(diretorio_atual + "\sounds\sem_internet_1.mp3")
        self.som_internet_caiu = pygame.mixer.Sound(diretorio_atual + "\sounds\caiu_internet_1.mp3")
        self.som_internet_voltou = pygame.mixer.Sound(diretorio_atual + "\sounds\internet_voltou.mp3")
        self.som_internet_caiu_dinovo = pygame.mixer.Sound(diretorio_atual + "\sounds\sem_internet_dinovo_1.mp3")

    # Função para a chamada do bloco que iniciará uma instância da classe NossaThread, responsável por executar uma
    # função em looping e ainda sim mostrar a tela incial do programa (mainWindow)
    def chamada_da_NossaThread(self):
        ##########################################################
        self.bloco = NossaThread()                               #
        self.bloco.set_function(self.check_internet_connection)  #
        self.bloco.start()                                       #
        ##########################################################

    # Função que coleta informações sobre a rede do usuário e mostra na mainWindow
    def busca_informacoes_rede(self):
        # Executa o comando ipconfig /all no Windows

        result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)

        # Se não obter erro no retorno, cria a lista output_lines, onde cada posição vai receber uma linha do retorno
        if result.returncode == 0:
            output_lines = result.stdout.split('\n')

            # Cria as variáves para capturar as linhas referentes às posições dos DNS no retorno que está na lista
            linha_dns1 = output_lines[25]
            linha_dns2 = output_lines[26]

            # Cria mais duas listas, e separa a linha tudo que vier depois dos ":" fica na posição 1 da nova lista.
            parts1 = linha_dns1.split(':', 1)
            parts2 = linha_dns2.split(':', 1)

            # Verifica se o tamanho da primeira lista (parts1) tem duas posições
            if len(parts1) >= 2:
                dns1 = parts1[1].strip()
                dns2 = parts2[0].strip()

            # Seta os labels da mainWindows com as informações referentes ao DNS1 e DNS2, respectivamente
            html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{dns1}</span></p></body></html>"
            self.lb_dns1_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))

            html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{dns2}</span></p></body></html>"
            self.lb_dns2_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))


        # Executa o comando ipconfig no Windows
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)

        # Verifica o resultado
        if result.returncode == 0:
            output_lines = result.stdout.split('\n')

            # Verifica se a lista tem pelo menos 11 linhas
            if len(output_lines) >= 11:
                linha_ipv6 = output_lines[7]
                linha_ip = output_lines[8]
                linha_mascara = output_lines[9]
                linha_gateway = output_lines[10]

                # Divide apenas no primeiro ":"
                parts = linha_ipv6.split(':', 1)
                parts2 = linha_ip.split(':', 1)
                parts3 = linha_mascara.split(':', 1)
                parts4 = linha_gateway.split(':', 1)

                # Verifica se a linha foi dividida em pelo menos 2 partes
                if len(parts) >= 2:
                    # Remove espaços extras e seta a variável ipv6 com a segunda posição da lista parts
                    ipv6 = parts[1].strip()
                else:
                    ipv6 = ""

                if len(parts2) >= 2:
                    ip = parts2[1].strip()
                else:
                    ip = ""

                if len(parts3) >= 2:
                    mascara = parts3[1].strip()
                else:
                    mascara = ""

                if len(parts4) >= 2:
                    gateway = parts4[1].strip()
                else:
                    gateway = ""

                # Seta os labels da mainWindows com os respectivos valores de ipv6, ip, mascara e gateway
                html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{ipv6}</span></p></body></html>"
                self.lb_ipv6_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))

                html_text = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{ip}</span></p></body></html>"
                self.lb_ip_resultado.setText(QCoreApplication.translate("MainWindow", html_text, None))

                html_text = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{mascara}</span></p></body></html>"
                self.lb_mascara_resultado.setText(QCoreApplication.translate("MainWindow", html_text, None))

                html_text = f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">{gateway}</span></p></body></html>"
                self.lb_gateway_resultado.setText(QCoreApplication.translate("MainWindow", html_text, None))

    # Função que checa se a internet está funcionando em looping e em cado de alguma mudança, ele avisa por áudio.
    def check_internet_connection(self):
        previous_status = None
        num_failures = 0

        while True:
            try:
                socket.create_connection(("www.google.com", 80))
                current_status = "Online"
            except OSError:
                current_status = "Offline"

            if previous_status is None:
                if current_status == "Online":
                    self.altera_img_internet_ok()
                    print("Status da Internet:", current_status)
                else:
                    self.altera_img_internet_nao_ok()
                    print("Status da Internet:", current_status)
            elif previous_status != current_status:
                if current_status == "Online":
                    self.altera_img_internet_voltou()
                    print("A Internet voltou!")
                else:
                    if num_failures < 1:
                        num_failures += 1
                        self.altera_img_internet_caiu()
                        print("A Internet caiu.")
                    elif num_failures >= 1:
                        self.altera_img_internet_caiu_dinovo()
                        print("A Internet caiu OUTRA VEZ.")

            previous_status = current_status
            time.sleep(5)

    # Função chamada pela função check_internet_connection em caso da internet estiver ok!
    def altera_img_internet_ok(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_verde_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Funcionando</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_ok, loops=0)

    # Função chamada pela função check_internet_connection em caso da internet não estiver ok!
    def altera_img_internet_nao_ok(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sem Internet</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_sem_internet, loops=0)

    # Função chamada pela função check_internet_connection em caso da internet cair!
    def altera_img_internet_caiu(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet caiu!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_caiu, loops=0)

    # Função chamada pela função check_internet_connection em caso da internet voltar!
    def altera_img_internet_voltou(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_verde_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet voltou!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_voltou, loops=0)

    # Função chamada pela função check_internet_connection em caso da internet cair a partir da segunda vez!
    def altera_img_internet_caiu_dinovo(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet caiu dinovo!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_caiu_dinovo, loops=0)



# Precisa de apenas uma instância por aplicação
app = QApplication(sys.argv)
# Criação do qtwidget que será a janela
window = MainWindow()
# Começa o evento loop
window.show()

app.exec_()
