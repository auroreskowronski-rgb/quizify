"""Quizify interface graphique module"""

import tkinter as tk

__author__ = "skowro_j"


class Window:
    """Classe représentant la fenêtre principale de l'application Quizify."""

    def __init__(self):
        """Initialise la fenêtre principale."""
        self.window = tk.Tk()
        self.window.title("Quizify")
        self.window.geometry("1024x720")
        self.window.resizable(False, False)
        self.window.configure(background="#FFAB52")

    def run(self):
        """Lance la boucle principale de la fenêtre."""
        self.window.mainloop()


class Cadre:
    """Classe représentant un label dans la fenêtre principale."""

    def __init__(self, master):
        """Initialise un cadre dans la fenêtre principale."""
        self.cadre = tk.Frame(master.window, bg="#FFAB52")
        self.cadre.pack(pady=10)

    def effacer_contenu(self):
        """Efface le contenu du cadre."""
        for widget in self.cadre.winfo_children():
            widget.destroy()


class Cadre2:
    """Classe représentant un deuxième cadre dans le 1er cadre."""

    def __init__(self, master):
        """Initialise un deuxième cadre dans le premier cadre (master)."""
        self.cadre = tk.Frame(master.cadre, bg="#FFAB52")
        self.cadre.pack(pady=10)


class Entry:
    """Classe représentant un champ de saisie dans la fenêtre principale."""

    def __init__(self, master):
        """Initialise un champ de saisie."""
        self.entry = tk.Entry(master.cadre, font=("Arial", 24))
        self.entry.pack(pady=10)


class Button_menu:
    """Classe représentant un bouton dans la fenêtre principale."""

    def __init__(self, master, text, command):
        """Initialise un bouton avec le texte spécifié."""
        self.bouton = tk.Button(
            master.cadre,
            text=text,
            font=("Arial", 24),
            bg="#52ABFF",
            width=40,
            command=command,
        )


class Titre:
    """Classe représentant le titre de l'application."""

    def __init__(self, master, text):
        """Initialise le titre."""
        self.label = tk.Label(
            master.cadre, text=text, font=("Arial", 32), bg="#FFAB52"
        )
        self.label.pack(pady=100)


class Pied:
    """classe representant le pied de page hors des cadres."""

    def __init__(self, cadre):
        """Initialise le pied de pageé"""
        self.label = tk.Label(
            cadre.cadre.master, font=("Arial", 24), bg="#FFAB52"
        )
        self.label.place(relx=0.5, rely=1.0, anchor="s", y=-20)

    def afficher(self, texte):
        """Met à jour le texte affiché."""
        self.label.configure(text=texte)

    def detruire(self):
        """Supprime l'étiquette."""
        self.label.destroy()


class Button_1(Button_menu):
    """Classe représentant le bouton commencer quiz."""

    def __init__(self, master, text, command):
        """Initialise le bouton spécifique avec le texte spécifié."""
        super().__init__(master, text, command=command)
        self.bouton.pack(pady=10)


class Button_2(Button_menu):
    """Classe représentant le bouton afficher les score quiz."""

    def __init__(self, master, command):
        """Initialise le bouton spécifique avec le texte spécifié."""
        super().__init__(master, "Scores", command=command)
        self.bouton.pack(pady=10)


class Button_3(Button_menu):
    """Classe représentant le bouton quitter quiz."""

    def __init__(self, master, command):
        """Initialise le bouton spécifique avec le texte spécifié."""
        super().__init__(master, "Quitter", command=command)
        self.bouton.pack(pady=10)


class Question:
    """Classe représentant une question dans le quiz."""

    def __init__(self, master, text):
        """Initialise une question avec le texte spécifié."""
        self.label = tk.Label(
            master.cadre,
            text=text,
            font=("Arial", 24),
            bg="#FFAB52",
            width=50,
            height=7,
        )
        self.label.pack(padx=10, pady=10)


class Choix:
    """Classe représentant un choix dans la fenêtre principale."""

    def __init__(self, master, text, command):
        """Initialise un bouton de choix avec le texte spécifié."""
        self.bouton = tk.Button(
            master.cadre,
            text=text,
            font=("Arial", 24),
            bg="#52ABFF",
            width=18,
            command=command,
        )


class Choix_1(Choix):
    """Classe représentant le premier choix."""

    def __init__(self, master, texte, command):
        """Initialise le premier choix avec le texte spécifié."""
        super().__init__(master, texte, command=command)
        self.bouton.grid(row=1, column=0, padx=10, pady=10)


class Choix_2(Choix):
    """Classe représentant le deuxième choix."""

    def __init__(self, master, texte, command):
        """Initialise le deuxième choix avec le texte spécifié."""
        super().__init__(master, texte, command=command)
        self.bouton.grid(row=1, column=1, padx=10, pady=10)


class Choix_3(Choix):
    """Classe représentant le troisième choix."""

    def __init__(self, master, texte, command):
        """Initialise le troisième choix avec le texte spécifié."""
        super().__init__(master, texte, command=command)
        self.bouton.grid(row=2, column=0, padx=10, pady=10)


class Choix_4(Choix):
    """Classe représentant le quatrième choix."""

    def __init__(self, master, texte, command):
        """Initialise le quatrième choix avec le texte spécifié."""
        super().__init__(master, texte, command=command)
        self.bouton.grid(row=2, column=1, padx=10, pady=10)


class Score:
    """Classe pour afficher le scoreboard."""

    def __init__(self, master, text):
        """Initialise le titre."""
        self.label = tk.Label(
            master.cadre,
            text=text,
            font=("Arial", 14),
            bg="#FFAB52",
            width=70,
            height=1,
        )
        self.label.pack(pady=1)
