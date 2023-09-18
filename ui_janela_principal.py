# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(782, 637)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 241, 219);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frm_informacoes = QFrame(self.centralwidget)
        self.frm_informacoes.setObjectName(u"frm_informacoes")
        self.frm_informacoes.setGeometry(QRect(190, 20, 291, 201))
        self.frm_informacoes.setStyleSheet(u"QFrame#frm_informacoes{\n"
"	border: 1px solid black;\n"
"	\n"
"}\n"
"\n"
"")
        self.frm_informacoes.setFrameShape(QFrame.StyledPanel)
        self.frm_informacoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_informacoes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_ip = QLabel(self.frm_informacoes)
        self.lb_ip.setObjectName(u"lb_ip")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_ip.sizePolicy().hasHeightForWidth())
        self.lb_ip.setSizePolicy(sizePolicy1)
        self.lb_ip.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.lb_ip)

        self.lb_ip_resultado = QLabel(self.frm_informacoes)
        self.lb_ip_resultado.setObjectName(u"lb_ip_resultado")

        self.horizontalLayout.addWidget(self.lb_ip_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_mascara = QLabel(self.frm_informacoes)
        self.lb_mascara.setObjectName(u"lb_mascara")
        sizePolicy1.setHeightForWidth(self.lb_mascara.sizePolicy().hasHeightForWidth())
        self.lb_mascara.setSizePolicy(sizePolicy1)
        self.lb_mascara.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_2.addWidget(self.lb_mascara)

        self.lb_mascara_resultado = QLabel(self.frm_informacoes)
        self.lb_mascara_resultado.setObjectName(u"lb_mascara_resultado")

        self.horizontalLayout_2.addWidget(self.lb_mascara_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_gateway = QLabel(self.frm_informacoes)
        self.lb_gateway.setObjectName(u"lb_gateway")
        sizePolicy1.setHeightForWidth(self.lb_gateway.sizePolicy().hasHeightForWidth())
        self.lb_gateway.setSizePolicy(sizePolicy1)
        self.lb_gateway.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_3.addWidget(self.lb_gateway)

        self.lb_gateway_resultado = QLabel(self.frm_informacoes)
        self.lb_gateway_resultado.setObjectName(u"lb_gateway_resultado")

        self.horizontalLayout_3.addWidget(self.lb_gateway_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_dns1 = QLabel(self.frm_informacoes)
        self.lb_dns1.setObjectName(u"lb_dns1")
        sizePolicy1.setHeightForWidth(self.lb_dns1.sizePolicy().hasHeightForWidth())
        self.lb_dns1.setSizePolicy(sizePolicy1)
        self.lb_dns1.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_4.addWidget(self.lb_dns1)

        self.lb_dns1_resultado = QLabel(self.frm_informacoes)
        self.lb_dns1_resultado.setObjectName(u"lb_dns1_resultado")

        self.horizontalLayout_4.addWidget(self.lb_dns1_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_dns2 = QLabel(self.frm_informacoes)
        self.lb_dns2.setObjectName(u"lb_dns2")
        sizePolicy1.setHeightForWidth(self.lb_dns2.sizePolicy().hasHeightForWidth())
        self.lb_dns2.setSizePolicy(sizePolicy1)
        self.lb_dns2.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_5.addWidget(self.lb_dns2)

        self.lb_dns2_resultado = QLabel(self.frm_informacoes)
        self.lb_dns2_resultado.setObjectName(u"lb_dns2_resultado")

        self.horizontalLayout_5.addWidget(self.lb_dns2_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_ipv6 = QLabel(self.frm_informacoes)
        self.lb_ipv6.setObjectName(u"lb_ipv6")
        sizePolicy1.setHeightForWidth(self.lb_ipv6.sizePolicy().hasHeightForWidth())
        self.lb_ipv6.setSizePolicy(sizePolicy1)
        self.lb_ipv6.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_6.addWidget(self.lb_ipv6)

        self.lb_ipv6_resultado = QLabel(self.frm_informacoes)
        self.lb_ipv6_resultado.setObjectName(u"lb_ipv6_resultado")

        self.horizontalLayout_6.addWidget(self.lb_ipv6_resultado)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.frm_status_internet = QFrame(self.centralwidget)
        self.frm_status_internet.setObjectName(u"frm_status_internet")
        self.frm_status_internet.setGeometry(QRect(10, 20, 171, 201))
        self.frm_status_internet.setStyleSheet(u"QFrame#frm_status_internet{\n"
"	border: 1px solid black;\n"
"\n"
"}")
        self.frm_status_internet.setFrameShape(QFrame.StyledPanel)
        self.frm_status_internet.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_status_internet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_status_da_conexao = QLabel(self.frm_status_internet)
        self.lb_status_da_conexao.setObjectName(u"lb_status_da_conexao")

        self.verticalLayout_2.addWidget(self.lb_status_da_conexao)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lb_nulo = QLabel(self.frm_status_internet)
        self.lb_nulo.setObjectName(u"lb_nulo")

        self.horizontalLayout_7.addWidget(self.lb_nulo)

        self.lb_img_status_conexao = QLabel(self.frm_status_internet)
        self.lb_img_status_conexao.setObjectName(u"lb_img_status_conexao")
        self.lb_img_status_conexao.setMaximumSize(QSize(141, 141))
        self.lb_img_status_conexao.setPixmap(QPixmap(u"images/sinal_amarelo_grande.png"))
        self.lb_img_status_conexao.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lb_img_status_conexao)

        self.lb_nulo_2 = QLabel(self.frm_status_internet)
        self.lb_nulo_2.setObjectName(u"lb_nulo_2")

        self.horizontalLayout_7.addWidget(self.lb_nulo_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.lb_status_da_conexao_resultado = QLabel(self.frm_status_internet)
        self.lb_status_da_conexao_resultado.setObjectName(u"lb_status_da_conexao_resultado")

        self.verticalLayout_2.addWidget(self.lb_status_da_conexao_resultado)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 590, 331, 41))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.btn_pingar = QPushButton(self.centralwidget)
        self.btn_pingar.setObjectName(u"btn_pingar")
        self.btn_pingar.setGeometry(QRect(320, 250, 41, 23))
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 230, 157, 41))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.ln_entrada_ping = QLineEdit(self.layoutWidget1)
        self.ln_entrada_ping.setObjectName(u"ln_entrada_ping")

        self.verticalLayout_4.addWidget(self.ln_entrada_ping)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(180, 230, 133, 41))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.ln_quantidade_ping = QLineEdit(self.layoutWidget2)
        self.ln_quantidade_ping.setObjectName(u"ln_quantidade_ping")

        self.verticalLayout_5.addWidget(self.ln_quantidade_ping)

        self.btn_abrir_janela_logs_conexao = QPushButton(self.centralwidget)
        self.btn_abrir_janela_logs_conexao.setObjectName(u"btn_abrir_janela_logs_conexao")
        self.btn_abrir_janela_logs_conexao.setGeometry(QRect(110, 550, 75, 23))
        self.btn_abrir_janela_logs_ping = QPushButton(self.centralwidget)
        self.btn_abrir_janela_logs_ping.setObjectName(u"btn_abrir_janela_logs_ping")
        self.btn_abrir_janela_logs_ping.setGeometry(QRect(190, 550, 75, 23))
        self.lbl_log_ping = QLabel(self.centralwidget)
        self.lbl_log_ping.setObjectName(u"lbl_log_ping")
        self.lbl_log_ping.setGeometry(QRect(10, 280, 351, 261))
        self.lbl_log_ping.setStyleSheet(u"QLabel#lbl_log_ping{\n"
"	border: 1px solid black;\n"
"\n"
"}")
        self.lbl_log_ping.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_dns_google = QPushButton(self.centralwidget)
        self.btn_dns_google.setObjectName(u"btn_dns_google")
        self.btn_dns_google.setGeometry(QRect(570, 20, 75, 23))
        self.btn_dns_auto = QPushButton(self.centralwidget)
        self.btn_dns_auto.setObjectName(u"btn_dns_auto")
        self.btn_dns_auto.setGeometry(QRect(490, 20, 75, 23))
        self.lbl_log_rede = QLabel(self.centralwidget)
        self.lbl_log_rede.setObjectName(u"lbl_log_rede")
        self.lbl_log_rede.setGeometry(QRect(490, 90, 281, 131))
        self.lbl_log_rede.setStyleSheet(u"QLabel#lbl_log_rede{\n"
"	border: 1px solid black;\n"
"\n"
"}")
        self.lbl_log_rede.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_ip.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">IP</span></p></body></html>", None))
        self.lb_ip_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">-</p></body></html>", None))
        self.lb_mascara.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">M\u00e1scara</span></p></body></html>", None))
        self.lb_mascara_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">-</span></p></body></html>", None))
        self.lb_gateway.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Gateway</span></p></body></html>", None))
        self.lb_gateway_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">-</span></p></body></html>", None))
        self.lb_dns1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DNS-1</span></p></body></html>", None))
        self.lb_dns1_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">-</span></p></body></html>", None))
        self.lb_dns2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DNS-2</span></p></body></html>", None))
        self.lb_dns2_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">-</span></p></body></html>", None))
        self.lb_ipv6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">IPV6</span></p></body></html>", None))
        self.lb_ipv6_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">-</span></p></body></html>", None))
        self.lb_status_da_conexao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Status da conex\u00e3o</span></p></body></html>", None))
        self.lb_nulo.setText("")
        self.lb_img_status_conexao.setText("")
        self.lb_nulo_2.setText("")
        self.lb_status_da_conexao_resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Verificando</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cad\u00ea minha internet?</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">by II Luiiz II</span></p></body></html>", None))
        self.btn_pingar.setText(QCoreApplication.translate("MainWindow", u"Pingar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Digite o site para realizar o ping:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de pings (min:1 max:19)", None))
        self.btn_abrir_janela_logs_conexao.setText(QCoreApplication.translate("MainWindow", u"Logs conex\u00e3o", None))
        self.btn_abrir_janela_logs_ping.setText(QCoreApplication.translate("MainWindow", u"Logs ping", None))
        self.lbl_log_ping.setText("")
        self.btn_dns_google.setText(QCoreApplication.translate("MainWindow", u"DNS Google", None))
        self.btn_dns_auto.setText(QCoreApplication.translate("MainWindow", u"DNS Auto", None))
        self.lbl_log_rede.setText("")
    # retranslateUi

