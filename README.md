# 🎮 Quizify

Quiz à thèmes avec **interface graphique (tkinter)**, développé en **Python**.

## Fonctionnalités
- Interface graphique tkinter : menu, choix du thème, questions, résultats
- 4 thèmes (Pokémon, Dofus, Minecraft, World of Warcraft), 10 questions chacun
- Questions tirées aléatoirement depuis un fichier JSON
- Minuteur par question
- Profils joueurs et historique des scores (JSON)
- Tableau des scores (CSV)

## Lancement
Python 3 avec tkinter (`sudo apt install python3-tk` sous Debian/Ubuntu) :
```bash
cd quiz_project
python3 main.py
```

## Structure
```
quiz_project/
├── main.py          point d'entrée
├── quizz.py         logique du quiz et écrans
├── utilis.py        composants graphiques tkinter
├── user.py          gestion des joueurs et scores
├── bonus/
│   ├── timer.py     minuteur
│   └── scoreboard.csv
└── data/
    ├── questions.json
    └── utilisateurs.json
```

## Ajouter des questions
Ajoute un objet dans `data/questions.json` avec les champs `id`, `theme`, `question`, `options`, `reponse` et `Commentaire`.
