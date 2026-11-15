"""Quizify user module"""

import json
import os
from datetime import date

__author__ = "skowro_j"

path_data = os.path.join(os.path.dirname(__file__), "data")
path_json_u = os.path.join(path_data, "utilisateurs.json")


class User:
    """Classe représentant un utilisateur du quiz."""

    def __init__(self, user_name):
        """Initialise un utilisateur avec ses données et le theme choisi."""
        self.nom = user_name.upper()
        self.score = 0

    def theme(self, theme):
        """theme choisi par l'utilisateur."""
        self.theme = theme

    def mettre_a_jour_score(self, score: int):
        """Met à jour le score de l'utilisateur."""
        self.score = score

    def inscription_utilisateur(self):
        """Inscrit l'utilisateur dans le fichier json utilisateur."""
        try:
            with open(path_json_u, "r") as f:
                utilisateurs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            utilisateurs = {}

        if self.nom not in utilisateurs:
            utilisateurs[self.nom] = {"score": []}

        utilisateurs[self.nom]["score"].append(
            {
                "theme": self.theme,
                "score": self.score,
                "date": str(date.today()),
            }
        )

        with open(path_json_u, "w") as f:
            json.dump(utilisateurs, f, indent=4)
