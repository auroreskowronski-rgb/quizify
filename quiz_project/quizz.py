"""Quizify quiz module"""

import csv
import json
import os
import random
import sys

import utilis
from bonus import timer
from user import User

__author__ = "skowro_j"


path_data = os.path.join(os.path.dirname(__file__), "data")
path_json = os.path.join(path_data, "questions.json")
path_json_u = os.path.join(path_data, "utilisateurs.json")
path_bonus = os.path.join(os.path.dirname(__file__), "bonus")
path_board = os.path.join(path_bonus, "scoreboard.csv")

nombre_questions = 10
duree_question = 8


class Data:
    """Classe pour gérer les données du quiz."""

    @staticmethod
    def generate_data_list(json_file) -> list:
        """Génère une liste de données à partir d'un fichier JSON.

        La liste est mélangée aléatoirement.
        """
        try:
            with open(json_file, "r") as f:
                data_list = json.load(f)
            random.shuffle(data_list)
            return data_list
        except FileNotFoundError:
            print(f"Le fichier {json_file} est introuvable.")
            return []
        except json.JSONDecodeError:
            print(f"Erreur lors de la lecture du fichier {json_file}.")
            return []

    @staticmethod
    def selection_question(data_list: list, theme: str) -> list:
        """Sélectionne les questions correspondant au thème."""
        if theme == "Tout":
            return data_list

        filtered_list = [data for data in data_list if data["theme"] == theme]
        if not filtered_list:
            print(f"Aucune question disponible pour le thème {theme}.")
        return filtered_list


class Question:
    """Classe représentant une question du quiz."""

    def __init__(self, data: dict):
        """Initialise une question avec ses données."""
        self.question = data["question"]
        self.choix = list(data["options"])
        random.shuffle(self.choix)
        self.choix_A = self.choix[0]
        self.choix_B = self.choix[1]
        self.choix_C = self.choix[2]
        self.choix_D = self.choix[3]
        self.reponse = data["reponse"]
        self.commentaire = data["Commentaire"]
        self.theme = data["theme"]

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
            score.ajouter_point()
        else:
            pass
        return reponse_utilisateur == self.reponse

    def demarrer_timer(self, duree: int = 5):
        """Démarre le minuteur pour la question."""
        self.duree = duree
        self.timer = timer.Timer(duree)
        self.timer.start()


class Score:
    """Classe représentant le score d'un utilisateur au quiz."""

    def __init__(self):
        """Initialise le score à zéro."""
        self.points = 0

    def ajouter_point(self):
        """Ajoute un point au score."""
        self.points += 1


class Menu:
    """Classe représentant le menu du quiz."""

    def afficher_menu(self, cadre):
        """Affiche le menu du quiz."""
        utilis.Cadre.effacer_contenu(cadre)
        utilis.Titre(cadre, "Menu")
        utilis.Button_1(
            cadre,
            "Commencer le quiz",
            command=lambda: self.traiter_option(cadre, "1"),
        )
        utilis.Button_2(cadre, command=lambda: self.traiter_option(cadre, "2"))
        utilis.Button_3(cadre, command=lambda: self.traiter_option(cadre, "3"))

    def traiter_option(self, cadre, option):
        """Agit en fonction de l'option choisi"""
        if option == "1":
            utilis.Cadre.effacer_contenu(cadre)
            self.demander_nom(cadre)

        elif option == "2":
            self.voir_score(cadre)

        elif option == "3":
            sys.exit()

    def demander_nom(self, cadre):
        """Demande le prénom de l'utilisateur."""
        utilis.Titre(cadre, "Entrez votre nom")
        self.entry = utilis.Entry(cadre)
        utilis.Button_1(
            cadre, "Valider", command=lambda: self.recuperer_nom(cadre)
        )

    def recuperer_nom(self, cadre):
        """Récupère le nom de l'utilisateur."""

        self.nom = self.entry.entry.get()
        global user_name
        global user
        global questions
        user_name = self.nom
        user = User(user_name)
        questions = Data.generate_data_list(path_json)
        utilis.Cadre.effacer_contenu(cadre)

        self.demander_theme(cadre)
        return self.nom

    def demander_theme(self, cadre):
        """Demande le thème de l'utilisateur."""
        utilis.Question(cadre, "Choisissez un thème")
        cadre2 = utilis.Cadre2(cadre)

        utilis.Choix_1(
            cadre2,
            "Pokemon",
            command=lambda: self.traiter_theme(cadre, "Pokemon"),
        )
        utilis.Choix_2(
            cadre2,
            "World of warcraft",
            command=lambda: self.traiter_theme(cadre, "World of warcraft"),
        )
        utilis.Choix_3(
            cadre2, "Dofus", command=lambda: self.traiter_theme(cadre, "Dofus")
        )
        utilis.Choix_4(
            cadre2,
            "Minecraft",
            command=lambda: self.traiter_theme(cadre, "Minecraft"),
        )

    def traiter_theme(self, cadre, theme):
        """Récupère le thème de l'utilisateur et lance les questions."""
        global questions
        self.theme = theme
        user.theme(theme)
        questions = Data.selection_question(questions, theme)
        self.total = min(nombre_questions, len(questions))
        self.numero = 0
        score.points = 0
        utilis.Cadre.effacer_contenu(cadre)
        self.demander_question(cadre)

    def demander_question(self, cadre):
        """Affiche la question courante avec ses 4 choix et son minuteur."""
        if self.numero >= self.total:
            self.fin_quiz(cadre)
            return

        self.question = Question(questions[self.numero])
        utilis.Question(
            cadre,
            f"Question {self.numero + 1}/{self.total} - "
            f"{self.question.theme}\n{self.question.question}",
        ).label.configure(wraplength=900)
        cadre2 = utilis.Cadre2(cadre)
        classes = [
            utilis.Choix_1,
            utilis.Choix_2,
            utilis.Choix_3,
            utilis.Choix_4,
        ]
        lettres = ["A", "B", "C", "D"]
        for classe, lettre, texte in zip(
            classes, lettres, self.question.choix
        ):
            classe(
                cadre2,
                texte,
                command=lambda lettre=lettre: self.traiter_reponse(
                    cadre, lettre
                ),
            )
        self.question.demarrer_timer(duree_question)
        if not hasattr(self, "pied") or not self.pied.label.winfo_exists():
            self.pied = utilis.Pied(cadre)
        self.actualiser_timer(cadre)

    def actualiser_timer(self, cadre):
        """Met à jour le temps restant en temps réel."""
        restant = self.question.timer.remaining()
        if restant <= 0:
            self.traiter_reponse(cadre, None)
            return
        self.pied.afficher(f"Temps restant : {restant:.1f} s")
        self.minuteur = cadre.cadre.after(
            100, lambda: self.actualiser_timer(cadre)
        )

    def traiter_reponse(self, cadre, lettre):
        """Vérifie la réponse (None = temps écoulé) et affiche le résultat."""
        cadre.cadre.after_cancel(self.minuteur)
        utilis.Cadre.effacer_contenu(cadre)
        if lettre is None:
            resultat = (
                "Temps écoulé !\n"
                f"La bonne réponse était : {self.question.reponse}"
            )
        elif self.question.verifier_reponse(lettre):
            resultat = "Bonne réponse !"
        else:
            resultat = (
                "Mauvaise réponse.\n"
                f"La bonne réponse était : {self.question.reponse}"
            )
        self.pied.afficher(f"Score : {score.points}/{self.total}")
        utilis.Question(
            cadre, f"{resultat}\n\n{self.question.commentaire}"
        ).label.configure(wraplength=900)
        utilis.Button_1(
            cadre, "Suivant", command=lambda: self.question_suivante(cadre)
        )

    def question_suivante(self, cadre):
        """Passe à la question suivante."""
        self.numero += 1
        utilis.Cadre.effacer_contenu(cadre)
        self.demander_question(cadre)

    def fin_quiz(self, cadre):
        """Affiche le score final et l'enregistre."""
        self.pied.afficher(f"Score final : {score.points}/{self.total}")
        user.mettre_a_jour_score(score.points)
        user.inscription_utilisateur()
        Scoreboard().creer_tableau()
        Scoreboard().ecrire_scoreboard()
        utilis.Question(
            cadre,
            f"Quiz terminé !\nScore : {score.points} sur {self.total}\n"
            f"Merci d'avoir joué, {user.nom} !",
        )
        utilis.Button_3(cadre, command=lambda: self.afficher_menu(cadre))

    def voir_score(self, cadre):
        """Permet à l'utilisateur de voir le score"""
        utilis.Cadre.effacer_contenu(cadre)
        utilis.Question(cadre, "Scores des utilisateurs :")
        utilis.Button_3(cadre, command=lambda: Menu().afficher_menu(cadre))
        try:
            with open(path_json_u, "r") as f:
                utilisateurs = json.load(f)

                for nom, data in utilisateurs.items():
                    for score_entry in data["score"]:
                        utilis.Score(
                            cadre,
                            f" {nom}, Thème: {score_entry['theme']}, "
                            f"Score: {score_entry['score']}, "
                            f"Date: {score_entry['date']}",
                        )
        except (FileNotFoundError, json.JSONDecodeError):
            utilis.Score(cadre, "Aucun score disponible.")


class Scoreboard:
    """Classe représentant le tableau des scores."""

    def creer_tableau(self):
        """Crée un tableau des scores s'il n'existe pas déjà."""
        if not os.path.exists(path_board):
            with open(path_board, "w", encoding="utf-8"):
                pass

    def ecrire_scoreboard(self):
        """Écrit scoreboard.csv à partir de utilisateurs.json,
        trié par score."""
        try:
            with open(path_json_u, "r", encoding="utf-8") as f:
                utilisateurs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Aucun score disponible.")
            return

        lignes = [
            [nom, entree["theme"], entree["score"], entree["date"]]
            for nom, data in utilisateurs.items()
            for entree in data["score"]
        ]
        lignes.sort(key=lambda ligne: ligne[2], reverse=True)

        with open(path_board, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Utilisateur", "Theme", "Score", "Date"])
            writer.writerows(lignes)


score = Score()


class Quiz:
    """Classe représentant le quiz."""
    # initialisation de la fenêtre du quiz
    def __init__(self):
        """Initialise le quiz et affiche le menu principal."""
        self.win = utilis.Window()
        self.cadre = utilis.Cadre(self.win)
        Menu().afficher_menu(self.cadre)
        self.win.run()
