from PySide6 import QtWidgets
import sys


class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BTS CIEL")
        self.resize(400, 200)

        self.create_layouts()
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_layouts(self):
        self.layoutH1 = QtWidgets.QHBoxLayout()  # Layout pour les options (somme/produit)
        self.layoutH2 = QtWidgets.QHBoxLayout()  # Layout pour Nombre 1
        self.layoutH3 = QtWidgets.QHBoxLayout()  # Layout pour Nombre 2
        self.layoutH4 = QtWidgets.QHBoxLayout()  # Layout pour le résultat
        self.layoutH5 = QtWidgets.QHBoxLayout()  # Layout pour les boutons Calculer et Effacer
        self.layoutH6 = QtWidgets.QHBoxLayout()  # Layout pour le bouton Quitter
        self.layoutV = QtWidgets.QVBoxLayout()  # Layout principal vertical

    def create_widgets(self):
        # Widgets pour le choix de l'opération
        self.radioBt_somme = QtWidgets.QRadioButton("Somme")
        self.radioBt_produit = QtWidgets.QRadioButton("Produit")
        self.radioBt_somme.setChecked(True)  # Sélection par défaut de la somme

        # Widgets pour la saisie des nombres
        self.Lblnb1 = QtWidgets.QLabel("Nombre 1:")
        self.nb1 = QtWidgets.QLineEdit()
        self.Lblnb2 = QtWidgets.QLabel("Nombre 2:")
        self.nb2 = QtWidgets.QLineEdit()

        # Widget pour afficher le résultat
        self.LblLasomme = QtWidgets.QLabel("Résultat:")
        self.resultat = QtWidgets.QLineEdit()
        self.resultat.setReadOnly(True)  # Résultat en lecture seule

        # Boutons
        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def add_widgets_to_layouts(self):
        # Ajout des widgets dans les layouts respectifs
        self.layoutH1.addWidget(self.radioBt_somme)
        self.layoutH1.addWidget(self.radioBt_produit)

        self.layoutH2.addWidget(self.Lblnb1)
        self.layoutH2.addWidget(self.nb1)

        self.layoutH3.addWidget(self.Lblnb2)
        self.layoutH3.addWidget(self.nb2)

        self.layoutH4.addWidget(self.LblLasomme)
        self.layoutH4.addWidget(self.resultat)

        self.layoutH5.addWidget(self.btn_Calculer)
        self.layoutH5.addWidget(self.btn_Effacer)

        self.layoutH6.addWidget(self.btn_Quitter)

        # Ajout des layouts horizontaux dans le layout vertical principal
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)

        # Définir le layout principal de la fenêtre
        self.setLayout(self.layoutV)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(self.close)
        self.btn_Effacer.clicked.connect(self.clear_fields)
        self.btn_Calculer.clicked.connect(self.calculate_result)

    def calculate_result(self):
        try:
            # Récupération des valeurs saisies
            num1 = float(self.nb1.text())
            num2 = float(self.nb2.text())

            # Vérification de l'option choisie et calcul
            if self.radioBt_somme.isChecked():
                result = num1 + num2
            else:
                result = num1 * num2

            # Affichage du résultat dans le QLineEdit
            self.resultat.setText(str(result))

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez entrer des nombres valides.")

    def clear_fields(self):
        self.nb1.clear()
        self.nb2.clear()
        self.resultat.clear()
        self.radioBt_somme.setChecked(True)  # Réinitialiser la sélection par défaut


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    form = MaFenetre()
    form.show()
    sys.exit(app.exec())

