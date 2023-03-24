# tic-tac-toe
Projet : Tic Tac Toe - LaPlateforme

Ce projet a pour but de créer un programme en Python qui permet de jouer au Tic Tac Toe. Le programme à deux modes de jouabilités : PVP et PVE.  

# Processus
## Tic Tac Toe

Le Tic Tac Toe à était crée avec une interface graphique à l'aide de la librairie Tkinter. 
Les différents modes de jouabilités pour être accédé dans le menu : 
- Play VS AI : qui contient de modes de difficultés Facile et Difficile
- Play VS Player: qui est un simple mode en PVP
- Et une option pour relancer la partie 


## AI
Le premier mode de difficulté pour l'IA est la facile, elle est va faire des choix aléatoires dans les cases vides restantes. 
Le deuxième mode de difficulté est le difficile qui se base sur l'algorithme de Minimax. 
L'objectif de l'algorithme est de trouver la meilleure stratégie pour maximiser les gains d'un joueur tout en minimisant les pertes potentielles.

L'algorithme fonctionne en simulant tous les coups possibles du joueur et de son adversaire jusqu'à un certain niveau de profondeur, et en évaluant chaque coup en fonction de sa capacité à maximiser les gains du joueur et à minimiser ses pertes potentielles. À chaque niveau de profondeur, l'algorithme alterne entre maximiser et minimiser, d'où son nom "minimax".

# Utilisation
## Création de l'environnement virtuel
Pour la mise en palce de l'environnement virtuel :

### Sur Windows :
Dans le Windows Powershell il faudra cloner le git.

Récupération du projet
        
        $ git clone https://github.com/isabelle-nobile/tic-tac-toe
        
Executer le programme
        
        $ cd tic-tac-toe
        $ python main.py

----------------------------------------------
### Sur MacOS ou Linux :
Dans le terminal, il faudra cloner le git.

Récupération du projet

        $ git clone https://github.com/isabelle-nobile/tic-tac-toe

Executer le programme

        $ cd tic-tac-toe
        $ python3 main.py