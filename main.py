from PySide6 import QtWidgets
import sys


class CalculatriceIMC(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BTS SNIR2 - Calculatrice + IMC")
        self.resize(400, 200)

        self.create_layouts()
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutV = QtWidgets.QVBoxLayout()
    def create_widgets(self):
        self.radio_imc = QtWidgets.QRadioButton("IMC")
        self.radio_calculatrice = QtWidgets.QRadioButton("Calculatrice")
        self.radio_imc.setChecked(True)
        self.Lbl_1 = QtWidgets.QLabel("Taille en cm")
        self.champ_1 = QtWidgets.QLineEdit(self)
        self.champ_1.setPlaceholderText("Saisir votre taille en cm")
        self.Lbl_2 = QtWidgets.QLabel("Poids en Kg")
        self.champ_2 = QtWidgets.QLineEdit(self)
        self.champ_2.setPlaceholderText("Saisir votre poids en Kg")
        self.label_resultat = QtWidgets.QLabel("L'IMC : ")
        self.bouton_calculer = QtWidgets.QPushButton("Calculer")
        self.bouton_quitter = QtWidgets.QPushButton("Quitter")

    def add_widgets_to_layouts(self):

        self.layoutH1.addWidget(self.radio_imc)
        self.layoutH1.addWidget(self.radio_calculatrice)
        self.layoutH2.addWidget(self.Lbl_1)
        self.layoutH2.addWidget(self.champ_1)
        self.layoutH3.addWidget(self.Lbl_2)
        self.layoutH3.addWidget(self.champ_2)
        self.layoutH4.addWidget(self.label_resultat)


        self.layoutH5.addWidget(self.bouton_calculer)
        self.layoutH5.addWidget(self.bouton_quitter)


        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)

        self.setLayout(self.layoutV)

    def setup_connections(self):
        self.radio_imc.toggled.connect(self.mettre_a_jour_interface)
        self.radio_calculatrice.toggled.connect(self.mettre_a_jour_interface)
        self.bouton_calculer.clicked.connect(self.calculer)
        self.bouton_quitter.clicked.connect(self.close)



    def mettre_a_jour_interface(self):
        if self.radio_imc.isChecked():
            self.Lbl_1.setText("Taille en cm")
            self.champ_1.setPlaceholderText("Saisir votre taille en cm")
            self.Lbl_2.setText("Poids en Kg")
            self.champ_2.setPlaceholderText("Saisir votre poids en kg")
            self.label_resultat.setText("IMC:")


        elif self.radio_calculatrice.isChecked():
            self.Lbl_1.setText("Nombre 1")
            self.champ_1.setPlaceholderText("Saisir un nombre")
            self.Lbl_2.setText("Nombre 2")
            self.champ_2.setPlaceholderText("Saisir un deuxieme nombre")
            self.label_resultat.setText("La somme:")




    def calculer(self):
        try:
            valeur_1 = float(self.champ_1.text())
            valeur_2 = float(self.champ_2.text())
            if self.radio_imc.isChecked():
                resultat = valeur_2 / ((valeur_1 / 100) ** 2)

                if resultat < 18.49 :
                    self.label_resultat.setText(f"IMC : {resultat:.2f} Vous etes maigre")
                if 18.50 < resultat < 24.99:
                    self.label_resultat.setText(f"IMC : {resultat:.2f} Vous etes normal")
                if 25.50 < resultat <29.99:
                    self.label_resultat.setText(f"IMC : {resultat:.2f} Vous etes en surpoids")
                if 30.00 < resultat  :
                    self.label_resultat.setText(f"IMC : {resultat:.2f} Vous etes obèse attention !!")
            elif self.radio_calculatrice.isChecked():
                resultat = valeur_1 + valeur_2
                self.label_resultat.setText(f"Somme : {resultat}")
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez entrer des valeurs numériques valides.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    fenetre = CalculatriceIMC()
    fenetre.show()
    sys.exit(app.exec())
