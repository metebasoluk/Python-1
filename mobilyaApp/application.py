from PyQt5 import QtCore, QtGui, QtWidgets,Qt
import sqlite3
import sys

connector = sqlite3.connect(database="urunTakip.db")
cursor = connector.cursor()

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.montajCount = 0
        self.count = 0
        self.siparisQuery=cursor.execute(f"select siparisID from siparisler")
        self.siparisNo=self.siparisQuery.fetchall()[-1][0]
        self.setObjectName("Form")
        self.resize(1001, 835)
        self.setWindowIcon(QtGui.QIcon("logo.ico"))
        self.setMaximumSize(1001,835)
        self.setMinimumSize(1001,835)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.setFont(font)
        self.logoLabel = QtWidgets.QLabel(self)
        self.logoLabel.setGeometry(QtCore.QRect(70, 10, 891, 191))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("logo.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.urunSecComboBox = QtWidgets.QComboBox(self)
        self.urunSecComboBox.setGeometry(QtCore.QRect(20, 290, 300, 41))
        self.urunSecComboBox.setObjectName("urunSecComboBox")
        for i in cursor.execute("select urunAdi from urunler").fetchall():
            self.urunSecComboBox.addItem(f"{i[0]}")
        self.urunSecLabel = QtWidgets.QLabel(self)
        self.urunSecLabel.setGeometry(QtCore.QRect(20, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.urunSecLabel.setFont(font)
        self.urunSecLabel.setObjectName("urunSecLabel")
        self.siparisOlusturButton = QtWidgets.QPushButton(self)
        self.siparisOlusturButton.setGeometry(QtCore.QRect(20, 340, 141, 41))
        self.siparisOlusturButton.setObjectName("siparisOlusturLabel")
        self.yapimAsamasTableView = QtWidgets.QTableWidget(self)
        self.yapimAsamasTableView.setGeometry(QtCore.QRect(20, 450, 961, 91))
        self.yapimAsamasTableView.setObjectName("yapimAsamasTableView")
        font1=QtGui.QFont()
        font1.setPointSize(8)
        self.yapimAsamasTableView.setFont(font1)
        self.yapimAsamasiLabel = QtWidgets.QLabel(self)
        self.yapimAsamasiLabel.setGeometry(QtCore.QRect(20, 400, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.yapimAsamasiLabel.setFont(font)
        self.yapimAsamasiLabel.setObjectName("yapimAsamasiLabel")
        self.sungerlendiButton = QtWidgets.QPushButton(self)
        self.sungerlendiButton.setGeometry(QtCore.QRect(20, 545, 111, 41))
        self.sungerlendiButton.setObjectName("sungerlendiButton")
        self.tamamlananSiparislerTableView = QtWidgets.QTableWidget(self)
        self.tamamlananSiparislerTableView.setGeometry(QtCore.QRect(20, 650, 961, 171))
        self.tamamlananSiparislerTableView.setObjectName("tamamlananSiparislerTableView")
        font2 = QtGui.QFont()
        font2.setPointSize(9)
        self.tamamlananSiparislerTableView.setFont(font2)
        self.tamamlananSiparislerLabel = QtWidgets.QLabel(self)
        self.tamamlananSiparislerLabel.setGeometry(QtCore.QRect(20, 600, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tamamlananSiparislerLabel.setFont(font)
        self.tamamlananSiparislerLabel.setObjectName("tamamlananSiparislerLabel")
        self.dosendiButton = QtWidgets.QPushButton(self)
        self.dosendiButton.setGeometry(QtCore.QRect(140, 545, 111, 41))
        self.dosendiButton.setObjectName("dosendiButton")
        self.montajlandButton = QtWidgets.QPushButton(self)
        self.montajlandButton.setGeometry(QtCore.QRect(260, 545, 111, 41))
        self.montajlandButton.setObjectName("montajlandButton")


        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "??r??n Takip Otomasyonu"))
        self.urunSecLabel.setText(_translate("Form", "??r??n Se??"))
        self.siparisOlusturButton.setText(_translate("Form", "Sipari?? Olu??tur"))
        self.yapimAsamasiLabel.setText(_translate("Form", "Yap??m A??amas??"))
        self.sungerlendiButton.setText(_translate("Form", "S??ngerlendi"))
        self.tamamlananSiparislerLabel.setText(_translate("Form", "Tamamlanan Sipari??ler"))
        self.dosendiButton.setText(_translate("Form", "D????endi"))
        self.montajlandButton.setText(_translate("Form", "Montajland??"))


        query = cursor.execute("select siparisID, urunAdi from siparisler").fetchmany(100)
        self.tamamlananSiparislerTableView.setRowCount(100)
        self.tamamlananSiparislerTableView.setColumnCount(2)
        self.tamamlananSiparislerTableView.setHorizontalHeaderLabels(["Sipari?? Numaras??","??r??n Ad??"])
        header = self.tamamlananSiparislerTableView.horizontalHeader()
        header.setStretchLastSection(True)

        for i in range(len(query)):
            self.tamamlananSiparislerTableView.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{query[i][0]}"))
            self.tamamlananSiparislerTableView.setItem(i, 1, QtWidgets.QTableWidgetItem(query[i][1]))





        self.siparisOlusturButton.clicked.connect(self.siparisOlusturFunch)
        self.sungerlendiButton.clicked.connect(self.sungerlendiFuch)
        self.dosendiButton.clicked.connect(self.dosendiFunch)
        self.montajlandButton.clicked.connect(self.montajlandFunch)


        self.show()

    def siparisOlusturFunch(self):
        query=cursor.execute(f"select * from urunler where urunAdi='{self.urunSecComboBox.currentText()}'")
        kanepeTuru=query.fetchone()[2]
        query = cursor.execute(f"select * from urunler where urunAdi='{self.urunSecComboBox.currentText()}'")
        berjerTuru = query.fetchone()[3]

        if kanepeTuru=="Mekanizmal??" and berjerTuru=="1GOS":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(11)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(["Sipari?? Numaras??","Kanepe S??rt","Kanepe Oturak","Kanepe Oturak 2","Kanepe Kol 1","Kanepe Kol 2","Berjer 1 S??rt","Berjer 1 G??vde","Berjer 1 Oturak","Berjer 2 S??rt","Berjer 2 G??vde","Berjer 2 Oturak"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 9, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 10, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))

        elif kanepeTuru=="Mekanizmal??" and berjerTuru=="2GO":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(10)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(
                ["Sipari?? Numaras??","Kanepe S??rt", "Kanepe Oturak", "Kanepe Oturak 2", "Kanepe Kol 1", "Kanepe Kol 2",
                 "Berjer 1 G??vde", "Berjer 1 Oturak","Berjer 2 G??vde", "Berjer 2 Oturak"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 9, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))

        elif kanepeTuru=="Mekanizmal??" and berjerTuru=="3GK":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(10)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(
                ["Sipari?? Numaras??","Kanepe S??rt", "Kanepe Oturak", "Kanepe Oturak 2", "Kanepe Kol 1", "Kanepe Kol 2",
                 "Berjer 1 G??vde", "Berjer 1 Kol","Berjer 2 G??vde", "Berjer 2 Kol"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 9, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))

        elif kanepeTuru=="Makasl??" and berjerTuru=="1GOS":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(11)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(
                ["Sipari?? Numaras??","Kanepe G??vde","Kanepe Kol 1","Kanepe Kol 2","Kanepe Kasa",
                 "Berjer 1 S??rt","Berjer 1 G??vde","Berjer 1 Oturak","Berjer 2 S??rt","Berjer 2 G??vde","Berjer 2 Oturak"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 9, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 10, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))


        elif kanepeTuru=="Makasl??" and berjerTuru=="2GO":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(9)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(
                ["Sipari?? Numaras??","Kanepe G??vde","Kanepe Kol 1","Kanepe Kol 2","Kanepe Kasa",
                 "Berjer 1 G??vde", "Berjer 1 Oturak","Berjer 2 G??vde", "Berjer 2 Oturak"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))


        elif kanepeTuru=="Makasl??" and berjerTuru=="3GK":
            self.yapimAsamasTableView.setRowCount(1)
            self.yapimAsamasTableView.setColumnCount(10)
            self.yapimAsamasTableView.setHorizontalHeaderLabels(
                ["Sipari?? Numaras??","Kanepe G??vde","Kanepe Kol 1","Kanepe Kol 2","Kanepe Kasa",
                 "Berjer 1 G??vde", "Berjer 1 Kol","Berjer 2 G??vde", "Berjer 2 Kol"])
            header = self.yapimAsamasTableView.horizontalHeader()
            header.setStretchLastSection(True)
            self.yapimAsamasTableView.setItem(0, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo+1}"))
            self.yapimAsamasTableView.setItem(0, 1, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 2, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 3, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 4, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 5, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 6, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 7, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 8, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))
            self.yapimAsamasTableView.setItem(0, 9, QtWidgets.QTableWidgetItem("Yap??m A??amas??nda"))



    def sungerlendiFuch(self):
        try:
            self.yapimAsamasTableView.selectedItems()[0].setText("S??ngerlendi")
        except:
            pass


    def dosendiFunch(self):
        try:
            self.yapimAsamasTableView.selectedItems()[0].setText("D????endi")
        except:
            pass


    def montajlandFunch(self):
        try:
            self.yapimAsamasTableView.selectedItems()[0].setText("Montajland??")
            for i in range(self.yapimAsamasTableView.selectedItems()[0].column(),self.yapimAsamasTableView.columnCount()):
                if self.yapimAsamasTableView.item(0,i).text()=="Montajland??":
                    self.montajCount+=1
            if self.montajCount>=self.yapimAsamasTableView.columnCount()-1:
                print("a")
                self.montajCount=0

                self.tamamlananSiparislerTableView.setRowCount(100)
                self.tamamlananSiparislerTableView.setColumnCount(2)
                self.tamamlananSiparislerTableView.setHorizontalHeaderLabels(["Sipari?? Numaras??","??r??n Ad??"])
                self.tamamlananSiparislerTableView.setItem(self.count, 0, QtWidgets.QTableWidgetItem(f"{self.siparisNo}"))
                self.tamamlananSiparislerTableView.setItem(self.count, 1, QtWidgets.QTableWidgetItem(self.urunSecComboBox.currentText()))
                self.siparisNo+=1
                self.count+=1
                print(self.siparisNo)
                print(type(self.siparisNo))
                print(self.urunSecComboBox.currentText())
                print(type(self.urunSecComboBox.currentText()))
                print(f"INSERT INTO siparisler (siparisID,urunAdi) VALUES ({self.siparisNo},'{self.urunSecComboBox.currentText()}')")
                cursor.execute(f"INSERT INTO siparisler (siparisID,urunAdi) VALUES ({self.siparisNo},'{self.urunSecComboBox.currentText()}')")
                connector.commit()
                query = cursor.execute("select siparisID, urunAdi from siparisler").fetchmany(100)
                for i in range(len(query)):
                    self.tamamlananSiparislerTableView.setItem(i, 0, QtWidgets.QTableWidgetItem(f"{query[i][0]}"))
                    self.tamamlananSiparislerTableView.setItem(i, 1, QtWidgets.QTableWidgetItem(query[i][1]))
        except:
            pass



class Window(QtWidgets.QWidget):
    def __int__(self):
        super(Window,self).__init__()
        self.ui=Ui()


app=QtWidgets.QApplication(sys.argv)
window=Ui()
sys.exit(app.exec_())