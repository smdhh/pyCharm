from PySide6 import QtWidgets
import sys


class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.LEdit_Brocker = None
        self.resize(600, 10)
        self.setWindowTitle("BTS CIEL")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()

    def create_layouts(self):

        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()
        self.layoutV = QtWidgets.QVBoxLayout()
    def create_widgets(self):
        self.lbl_somme= QtWidgets.QLabel("Somme")
        self.lEdit_somme= QtWidgets.QLineEdit("Somme")
        self.radioBt_somme = QtWidgets.QRadioButton()

        self.lbl_produit = QtWidgets.QLabel("Produit")
        self.radioBt_produit = QtWidgets.QRadioButton("Produit")
        self.LEdit_Produit = QtWidgets.QLineEdit()

        self.Lblnb1 = QtWidgets.QLabel("Nombre 1 ")
        self.nb1 = QtWidgets.QLineEdit("")
        self.Lblnb2 = QtWidgets.QLabel("Nombre 2 ")
        self.nb2 = QtWidgets.QLineEdit("")
        self.LblLasomme = QtWidgets.QLabel("La somme ")
        self.Lasomme = QtWidgets.QLabel(".......")






        self.Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setStyleSheet("background-color: black; color: white;")
        self.radioBt_somme.setChecked(True)
        self.Lasomme.setDisabled(True)

    def addWigets_to_layouts(self):

        self.layoutH1.addWidget(self.radioBt_somme)
        self.layoutH1.addWidget(self.lEdit_somme)
        self.layoutH1.addWidget(self.radioBt_produit)
        self.layoutH1.addWidget(self.LEdit_Produit)

        self.layoutH2.addWidget(self.Lblnb1)
        self.layoutH2.addWidget(self.nb1)
        self.layoutH3.addWidget(self.Lblnb2)
        self.layoutH3.addWidget(self.nb2)
        self.layoutH4.addWidget(self.LblLasomme)
        self.layoutH4.addWidget(self.Lasomme)
        self.layoutH5.addWidget(self.Calculer)
        self.layoutH5.addWidget(self.btn_Effacer)


        self.layoutH6 = QtWidgets.QHBoxLayout()
        self.layoutH6.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutV)

        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
    def Somme (self):
        if self.radioBt_somme.isChecked():
            print("Somme")
            self.Lasomme.setDisabled(False)


    def Produit(self):
        if self.radioBt_produit.isChecked():
            print("Produit")
            self.Lasomme.setDisabled(True)


    def clear_Ledit(self):
        self.LEdit_Brocker.setText("")


if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()