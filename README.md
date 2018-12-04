TP07 Modèle d'avalanches
========================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Spécifications
--------------


On va représenter la montagne par une liste contenant la hauteur de
chacune des colonnes. Par exemple, la configuration initiale de
l’exemple introductif serait `[6,6,5,2,1]`.

Il vous faut à présent écrire (et documenter !) les fonctions suivantes:


1.  `il_neige(montagne,position)` rajoute un bloc de neige à l’indice `position` de la liste `montagne`. Elle se contente de modifier `montagne` et ne renvoie rien (`None`).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  `est_instable(montagne)` renvoie `True` s’il existe des colonnes instables (à droite ou à gauche)
    dans la liste `montagne` et `False` sinon. Une colonne est dite instable si sa taille
    excède strictement de deux unités celle d’une de ses voisines.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  `relaxation(montagne)` Fait *une* étape de relaxation, c’est-à-dire qu’on déplace deux
    blocs de toutes les colonnes instables vers les colonnes voisines
    (elle modifie donc la liste `montagne`). La montagne est supposée être adossée
    à un mur à gauche, mais être au bord d’un abysse à droite. La
    fonction renvoie le nombre de blocs qui tomberait dans l’abysse au
    cours de l’expérience. Exemple: `relaxation([6,6,5,2,1])` modifie la liste en `[6,6,3,4,1]` et renvoie `0` (car
    aucun bloc ne tombe dans l’abysse). De même `relaxation([6,4,5,2,3])` modifie la liste en `[6,4,3,4,1]` et
    renvoie `2` (deux blocs sont tombés dans l’abîme).

    Remarque: On va supposer qu’un léger vent souffle vers l’abîme, de
    sorte que si une colonne est à la fois instable à droite *et* à
    gauche, elle privilégie toujours le côté droit.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  `relaxation_totale(montagne)`   prend une montagne instable en entrée et procède à toutes les
    relaxations nécessaires tant que la montagne n’est pas devenue
    stable. Elle renvoie le nombre total de blocs tombés lors du
    processus. Exemple: `relaxation_totale([6,6,5,2,1])` modifie la liste en `[6,4,3,2,1]` et renvoie `4` (cf exemple
    introductif).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Une fois ces fonctions écrites, il devrait être facile de les mettre
ensemble pour répondre à la question posée, c’est-à-dire tracer D(S)
qui correspond au nombre D d’avalanches d’une taille S donnée en
s’aidant de la fonction `plt.hist()` de matplotlib (`help(plt.hist)` pour plus de détails). Exemple
d’utilisation:

```Python
import matplotlib.pyplot as plt    # Pour les graphes
import random                      # Pour tirer des notes au hasard
# Gaussienne de moyenne 10 et écart-type 3 pour toutes les PCSI
notes = [random.gauss(10,3) for k in range(130)]
# Dessin de l’histogramme avec 20 bins
# (on suppose de ce fait que personne n’aura pile 20/20... [ou plus !])
plt.hist(notes,bins=20,range=(0,20),cumulative=True,label=“Mode cumulatif”)
plt.hist(notes,bins=20,range=(0,20),label=“Notes des 3 PCSI”)
plt.title(’Quelques histogrammes’) # Le titre
plt.legend(loc=’upper left’)       # Les légendes
plt.savefig(’hist.png’)            # Sauvegarde
plt.clf()                          # Nettoyage
```

Stockez le graphique résultant sous le nom `TP07_avalanche_VotreNom` (en remplaçant bien sûr par
votre propre nom). Pensez à aussi mettre votre nom dans le titre du
graphique.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
