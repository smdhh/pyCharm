from PySide6 import QtWidgets
import sys


class MaFenetre(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Texte message")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV3 = QtWidgets.QVBoxLayout()
        self.layoutV4 = QtWidgets.QVBoxLayout()
        self.layoutV5 = QtWidgets.QVBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()


    def create_widgets(self):
        self.radioBt_activer = QtWidgets.QRadioButton("Durée")
        self.radioBt_desactiver = QtWidgets.QRadioButton("HDD")
        self.lbl_Taille = QtWidgets.QLabel("Taille")
        self.LEdit_Taille = QtWidgets.QLineEdit()
        self.LEdit_Taille.setPlaceholderText("")
        self.lbl_ips = QtWidgets.QLabel("ips")
        self.LEdit_ips= QtWidgets.QLineEdit()
        self.LEdit_ips.setPlaceholderText("")
        self.lbl_Hdd = QtWidgets.QLabel("Hdd")
        self.LEdit_Hdd = QtWidgets.QLineEdit()
        self.LEdit_Hdd.setPlaceholderText("")
        self.lbl_Duree = QtWidgets.QLabel("Durée")
        self.LEdit_Duree = QtWidgets.QLineEdit()
        self.LEdit_Duree.setPlaceholderText("")
        self.btn_Effacer = QtWidgets.QPushButton("Calculer")
        self.btn_Quitter = QtWidgets.QPushButton("Exit")

    def addWigets_to_layouts(self):
        self.layoutH0.addWidget(self.radioBt_activer)
        self.layoutH0.addWidget(self.radioBt_desactiver)

        self.layoutH1.addWidget(self.lbl_Taille)
        self.layoutH1.addWidget(self.LEdit_Taille)

        self.layoutH2.addWidget(self.lbl_ips)
        self.layoutH2.addWidget(self.LEdit_ips)

        self.layoutH3.addWidget(self.lbl_Hdd)
        self.layoutH3.addWidget(self.LEdit_Hdd)

        self.layoutV1.addWidget(self.lbl_Duree)
        self.layoutV2.addWidget(self.LEdit_Duree)
        self.layoutV3.addWidget(self.LEdit_Duree)
        self.layoutV4.addWidget(self.LEdit_Duree)
        self.layoutV5.addWidget(self.LEdit_Duree)
        self.layoutH5.addWidget(self.btn_Effacer)
        self.layoutH5.addWidget(self.btn_Quitter)
        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV1.addLayout(self.layoutV1)
        self.layoutV2.addLayout(self.layoutV2)
        self.layoutV3.addLayout(self.layoutV3)
        self.layoutV4.addLayout(self.layoutV4)
        self.layoutV5.addLayout(self.layoutV5)
        self.layoutV.addLayout(self.layoutH5)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)

    def clear_Ledit(self):
        self.LEdit_Nom.setText("")


if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()