#!/usr/bin/env python3
"""Script principal"""

import csv
import os
import random
import sys

__author__ = "skowro_j"


def generate_data_list(csv_file) -> list:
    """Génère une liste de données à partir d'un fichier CSV"""
    data_list = []
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader, None)
        for ligne in reader:
            data_list.append(tuple(ligne))
        random.shuffle(data_list)
        return data_list




# ----------------------------------------------------------------------------
path_ressources = os.path.join(os.path.dirname(__file__), "ressources")
path_csv = os.path.join(path_ressources, "culture_generale.csv")

# ----------------------------------------------------------------------------
class Question:
    """Classe représentant une question du quiz."""

    def __init__(self, data: tuple):
        """Initialise une question avec ses données."""
        self.question = data[0]
        self.choix = list(data[1:5])
        random.shuffle(self.choix)
        self.choix_A = self.choix[0]
        self.choix_B = self.choix[1]
        self.choix_C = self.choix[2]
        self.choix_D = self.choix[3]
        self.reponse = data[5]
        self.commentaire = data[6]
        self.theme = data[7]

    def afficher_question(self):
        """Affiche la question et les choix de réponse."""
        print(f"Question: {self.question}")
        print(
            f"Choix: \n A. {self.choix_A} \n B. {self.choix_B} \n C. {self.choix_C} \n D. {self.choix_D}"
        )

    def verifier_reponse(self, reponse_utilisateur: str) -> bool:
        """Vérifie si la réponse de l'utilisateur est correcte."""
        reponse_utilisateur = reponse_utilisateur.upper()
        if reponse_utilisateur == "A":
            reponse_utilisateur = self.choix_A
        elif reponse_utilisateur == "B":
            reponse_utilisateur = self.choix_B
        elif reponse_utilisateur == "C":
            reponse_utilisateur = self.choix_C
        elif reponse_utilisateur == "D":
            reponse_utilisateur = self.choix_D
        if reponse_utilisateur == self.reponse:
            print("Bonne réponse !")
            score.ajouter_point()
        else:
            print("Mauvaise réponse.")
            print(f"La bonne réponse était: {self.reponse}")
        return reponse_utilisateur == self.reponse

    def afficher_commentaire(self):
        """Affiche le commentaire associé à la question."""
        print(f"{self.commentaire}")

class Score:
    """Classe représentant le score d'un utilisateur au quiz."""

    def __init__(self):
        """Initialise le score à zéro."""
        self.points = 0

    def ajouter_point(self):
        """Ajoute un point au score."""
        self.points += 1

    def afficher_score(self):
        """Affiche le score actuel."""
        print(f"Score: {self.points}")

# ---------Boucle de quiz---------

score = Score()
def jouer_quiz():
    """Fonction principale pour jouer au quiz."""
    nombre_questions = 5
    questions = generate_data_list(path_csv)
    for _ in range(min(nombre_questions, len(questions))):
        print(f"Question {_ + 1} sur {nombre_questions}")
        question = Question(questions[-1])
        question.afficher_question()
        reponse_utilisateur = input("Votre réponse (A, B, C, D) : ")
        question.verifier_reponse(reponse_utilisateur)
        question.afficher_commentaire()
        score.afficher_score()
        questions.pop()

    print("Quiz terminé !")
    score.afficher_score()

jouer_quiz()
