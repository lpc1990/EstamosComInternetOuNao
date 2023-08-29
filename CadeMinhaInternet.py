# comando para converter arquivos UI criados pelo UI Designer para um arquivo .py:
# pyside2-uic arquivo.ui -o ui_arquivo.py (ui_arquivo.py - esse ui é somente uma referência
# de nome pra indicar a origem  do arquivo, dizendo que esse arquivo .py foi convertido de um arquivo .ui)

from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QIcon, QIntValidator
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QDialog, QFileDialog, QMessageBox
from ui_janela_principal import Ui_MainWindow
from ui_janela_log import Ui_janela_log
from datetime import datetime
import socket, time, pygame, subprocess, sys, os, tempfile


# Pega o diretório atual da execução do arquivo atual e joga o path dele na variável diretorio_atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
print("Diretório atual:", diretorio_atual)

# ____________________________________ Sessão da classe da  threads ____________________________________
# Classe que trabalha com Thread, que é a execução de funções sem travar o programa. Se quiser que uma função seja
# executada sem travar o sistema, deve-se criar uma isntância dessa classe para rodar a função.
class NossaThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.func = None

    def __del__(self):
        self.wait()

    def set_function(self, func, param=None, param2=None):
        self.func = func
        self.param = param
        self.param2 = param2

    def run(self):
        if self.param == None:
            # print("Sem parâmetro!")
            if self.func:
                self.func()
        elif self.param != None and self.param2 == None:
            if self.func:
                # print("Com parâmetro!")
                self.func(self.param)
        else:
            if self.param != None and self.param2 != None:
                self.func(self.param, self.param2)


# ____________________________________ Sessão da janela principal ____________________________________
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadê minha internet?")
        self.setWindowIcon(QIcon(diretorio_atual + "\images\icon.png"))
        self.setFixedSize(534, 659)
        self.busca_informacoes_rede()
        self.definindo_sons()
        self.chamada_da_NossaThread()
        self.chamada_da_NossaThread3()


        # Criação da lista para o log
        self.lista_log_conexao = []
        self.lista_log_ping = []


        self.ln_quantidade_ping.setValidator(QIntValidator())
        self.ln_quantidade_ping.textChanged.connect(self.teste_valor_quantidade_ping)

        # Botão pingar
        self.btn_pingar.clicked.connect(self.test_site_ip_valido_ping)

        # Botão abrir pagina de logs
        self.btn_abrir_janela_logs_conexao.clicked.connect(self.mostrar_janela_log_conexao)
        self.btn_abrir_janela_logs_ping.clicked.connect(self.mostrar_janela_log_ping)


        # ____________________________________ Sessão do tray do windows ____________________________________
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(diretorio_atual + "\images\icon.png"))
        self.tray_icon.setToolTip("Cadê minha internet?")

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



    # ____________________________________ Sessão de threads ____________________________________
    # Função para a chamada do bloco que iniciará uma instância da classe NossaThread, responsável por executar uma
    # função em looping e ainda sim mostrar a tela incial do programa (mainWindow)
    def chamada_da_NossaThread(self):
        ##########################################################
        self.bloco = NossaThread()                               #
        self.bloco.set_function(self.check_internet_connection)  #
        self.bloco.start()                                       #
        ##########################################################

    # Função para a chamada do bloco que iniciará uma instância da classe NossaThread, responsável por executar uma
    # função que capta o ping e o exibe na label)
    def chamada_da_NossaThread2(self):
        #############################################################################################
        self.bloco2 = NossaThread()                                                                 #
        self.bloco2.set_function(self.test_verbose_ping, self.hostname, self.quantidade_de_ping)    #
        self.bloco2.start()                                                                         #
        #############################################################################################

    # Função para a chamada do bloco que iniciará uma instância da classe NossaThread, responsável por executar uma
    # função que capta o ping pela primeira vez ao iniciar o programa
    def chamada_da_NossaThread3(self):
        #############################################################################################
        self.hostname = "www.google.com.br"                                                         #
        self.quantidade_de_ping = 4                                                                 #
        self.bloco3 = NossaThread()                                                                 #
        self.bloco3.set_function(self.test_verbose_ping, self.hostname, self.quantidade_de_ping)    #
        self.bloco3.start()                                                                         #
        #############################################################################################


    # ____________________________________ Sessão de funções principais ____________________________________
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

    # Função que pega o site e a quantidade de pings passada atraves da função da thread executada, e gera os
    # resultados dos pings
    def test_verbose_ping(self, hostname, quantidade_de_ping):
        self.bloquear_btnPing_lnPing()

        temp_file = tempfile.NamedTemporaryFile(delete=False)

        try:
            subprocess.run(["ping", "-n", str(quantidade_de_ping), hostname], stdout=temp_file)
        except Exception as e:
            print(f"Failed to perform verbose ping: {e}")
        finally:
            temp_file.close()

        with open(temp_file.name, 'r') as file:
            captured_output = file.read()

        os.unlink(temp_file.name)

        # Convertendo bytes para str usando decode()
        captured_output_str = str(captured_output)

        # Separar as linhas relevantes
        lines = captured_output_str.splitlines()

        # Filtrar as linhas que contêm "Resposta"
        response_lines = [line for line in lines if "Resposta" in line]

        # Juntar as linhas filtradas novamente em uma string
        formatted_output = '\n'.join(response_lines)
        self.adiciona_ao_log_ping(formatted_output, str(self.ln_entrada_ping.text()))
        self.lbl_resultado_ping.setText(formatted_output)

        # Roda a função de liberar as linhas após a execução da função de ping
        self.liberar_lnPing()

        # Limpa o campo ln_quantidade_ping após a execução da função de ping
        self.ln_quantidade_ping.setText("")

        # Após qualquer inserção de texto ou números nos campos abaixo, irá chamar a função para testar se pode ou não
        # liberar o botão de pingar. Só irá liberar se os dois campos estiverem preenchidos.
        self.ln_entrada_ping.textChanged.connect(self.bloquear_botao_ping)
        self.ln_quantidade_ping.textChanged.connect(self.bloquear_botao_ping)

        # Retorno da funçao
        return formatted_output

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

    # Testa se a quantidade inserida no campo ln_quantidade_ping é entre 1 e 19. Se não for, ele automáticamente
    # preenche com um dos valores, ou o mais alto ou o mais baixo
    def teste_valor_quantidade_ping(self, text):
        valor_minimo = 1
        valor_maximo = 19

        try:
            valor = int(text)
            if valor < valor_minimo:
                self.ln_quantidade_ping.setText(str(valor_minimo))
            elif valor > valor_maximo:
                self.ln_quantidade_ping.setText(str(valor_maximo))
        except ValueError:
            pass

    # Testa se a o site digitano no campo do ping é válido
    def test_site_ip_valido_ping(self):
        self.hostname = self.ln_entrada_ping.text()  #
        self.quantidade_de_ping = self.ln_quantidade_ping.text()

        try:
            # Verifica se é um IP válido
            socket.inet_aton(self.hostname)

            # Realize o teste de ping aqui
            self.chamada_da_NossaThread2()
        except socket.error:
            # Se não for um IP válido, tente resolver como um nome de domínio
            try:
                socket.gethostbyname(self.hostname)

                # Realize o teste de ping aqui
                self.chamada_da_NossaThread2()
            except socket.gaierror:
                # Se não for um nome de domínio válido, mostre uma mensagem de erro
                self.lbl_resultado_ping.setText("Domínio ou IP inválido!")

    # Função que chama a janela de log acionada pelo botão logs (btn_abrir_janela_logs)
    def mostrar_janela_log_conexao(self):
        self.log_windows = LogWindow(self.lista_log_conexao)
        self.historico_log = "\n".join(self.lista_log_conexao)
        self.log_windows.ptx_log.setPlainText(self.historico_log)
        self.log_windows.exec_()

    def mostrar_janela_log_ping(self):
        self.log_windows = LogWindow(self.lista_log_ping)
        self.historico_log = "\n".join(self.lista_log_ping)
        self.log_windows.ptx_log.setPlainText(self.historico_log)
        self.log_windows.exec_()


    # Adiciona o evento ao log (Está sendo chamado cada vez que a internet cai, volta, etc, na função de trocar imagem
    # e executar os sons.
    def adiciona_ao_log_conexao(self, evento):
        log = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.lista_log_conexao.append(f"{log}: {evento}")

    def adiciona_ao_log_ping(self, evento, site_pingado):
        log = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        if site_pingado == "":
            site = "www.google.com.br - Padrão primeiro ping"
        else:
            site = str(site_pingado)
            print(site)
        self.lista_log_ping.append(f"{log} ({site}): \n{evento}")


    # ____________________________________ Sessão de funções de alteração da img da internet ________________
    # Função chamada pela função check_internet_connection em caso da internet estiver ok!
    def altera_img_internet_ok(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_verde_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Funcionando</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_ok, loops=0)
        self.adiciona_ao_log_conexao("Internet funcionando na primeira execução do programa")

    # Função chamada pela função check_internet_connection em caso da internet não estiver ok!
    def altera_img_internet_nao_ok(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Sem Internet</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_sem_internet, loops=0)
        self.adiciona_ao_log_conexao("Sem Internet na primeira execução do programa")

    # Função chamada pela função check_internet_connection em caso da internet cair!
    def altera_img_internet_caiu(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet caiu!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_caiu, loops=0)
        self.adiciona_ao_log_conexao("Internet caiu")

    # Função chamada pela função check_internet_connection em caso da internet voltar!
    def altera_img_internet_voltou(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_verde_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet voltou!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_voltou, loops=0)
        self.adiciona_ao_log_conexao("Internet voltou")

    # Função chamada pela função check_internet_connection em caso da internet cair a partir da segunda vez!
    def altera_img_internet_caiu_dinovo(self):
        self.show_window() # Exibe a janela do programa se ele estiver no tray
        self.lb_img_status_conexao.setPixmap(diretorio_atual + '\images\sinal_vermelho_grande.png')
        html_text1 = f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">A Internet caiu dinovo!</span></p></body></html>"
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", html_text1, None))
        self.sons.play(self.som_internet_caiu_dinovo, loops=0)
        self.adiciona_ao_log_conexao("Internet caiu dinovo")


    # ____________________________________ Sessão de bloqueio de botões e linhas  _____________________________
    # Função para bloquear as entradas de linha e botão referenets ao ping. Essa função também é responsável por criar
    # e mensagem de processando ping na lb de exibição de ping
    def bloquear_btnPing_lnPing(self):
        texto_processando_ping = "Processando ping para " + self.hostname
        self.lbl_resultado_ping.setText(texto_processando_ping)
        self.btn_pingar.setDisabled(True)
        self.ln_entrada_ping.setDisabled(True)
        self.ln_quantidade_ping.setDisabled(True)

    # Função para liberar as entradas de linha referentes ao ping (site e quantidade de pings)
    def liberar_lnPing(self):
        self.ln_entrada_ping.setEnabled(True)
        self.ln_quantidade_ping.setEnabled(True)

    # Função que libera somente o botão de pingar
    def bloquear_botao_ping(self):
        habilitado = bool(self.ln_entrada_ping.text() and self.ln_quantidade_ping.text())
        self.btn_pingar.setEnabled(habilitado)



# Classe da janela de log
class LogWindow(QDialog, Ui_janela_log):
    def __init__(self, lista_log):
        super(LogWindow, self).__init__()
        self.setupUi(self)
        self.lista_log = lista_log

        self.setWindowTitle("Cadê minha internet? - Logs")
        self.setWindowIcon(QIcon(diretorio_atual + "\images\icon.png"))
        self.setFixedSize(535, 505)

        self.btn_exportar_log.clicked.connect(self.exportar_log)

    # Função que gera o txt do log.
    def exportar_log(self):
        self.historico_log = "\n".join(self.lista_log)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Exportar Log", "",
                                                   "Arquivos de Texto (*.txt);;Todos os Arquivos (*)",
                                                   options=options)

        if file_name:
            try:
                file_name += ".txt"
                with open(file_name, 'w') as file:
                    file.write(self.historico_log)
                self.mostrar_mensagem("Log exportado com sucesso para:\n" + file_name)
            except Exception as e:
                self.mostrar_mensagem("Erro ao exportar o log:\n" + str(e))

    # Função para mostrar uma mensagem para o usuário na tela
    def mostrar_mensagem(self, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle("Mensagem")
        msg_box.exec_()





# Precisa de apenas uma instância por aplicação
app = QApplication(sys.argv)
# Criação do qtwidget que será a janela
window = MainWindow()
# Começa o evento loop
window.show()

app.exec_()
