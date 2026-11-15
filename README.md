# 🎓 Quizify

Quiz de culture générale en ligne de commande, écrit en **Python**.

## Fonctionnalités
- Questions à choix multiples (A, B, C, D) avec ordre des réponses mélangé
- Questions tirées aléatoirement depuis un fichier CSV
- Explication après chaque réponse et affichage du score final
- Questions faciles à ajouter ou modifier dans `ressources/culture_generale.csv`

## Lancement
Aucune dépendance, Python 3 suffit :
```bash
python3 quizify.py
```

## Ajouter des questions
Format du CSV (séparateur `;`) :
```
Question;Option 1;Option 2;Option 3;Option 4;Bonne Reponse;Explication;Theme
```

## Structure
```
quizify.py                       programme principal (classes Question, Score)
ressources/culture_generale.csv  base de questions
```
