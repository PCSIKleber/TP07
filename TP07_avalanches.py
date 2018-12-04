# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des
# tests automatiquement et sans effort: il suffira de decommenter la ligne if
# if __name__ == '__main__': testeur.fais_tests('...')
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est
# ***absolument primordial*** de lancer l'execution dans le menu via
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP07 as testeur


# ***************************************************************************
# Tombe la neige... Tu ne viendras pas ce soir...
# ***************************************************************************

def il_neige(montagne,position):
    '''Rajoute un bloc de neige a l'indice 'position' de la liste 'montagne'.
    La fonction se contente de modifier 'montagne' et ne renvoie rien.'''

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_neige')

# ***************************************************************************
# Y a-t-il un risque a planter le baton sur cette pente ?
# ***************************************************************************

def est_instable(montagne):
    '''Renvoie 'True' s'il existe des colonnes instables (a droite ou a
    gauche) dans la liste 'montagne' et 'False' sinon. Une colonne est dite
    instable si sa taille excede strictement de deux unites celle d'une de ses
    voisines. NB: pour gagner du temps, on s'arrete des que possible.'''

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_est_instable')

# ***************************************************************************
# Badaboum.
# ***************************************************************************

def relaxation(montagne):
    '''Fait *une* etape de relaxation, c'est-a-dire qu'on deplace deux blocs
    de toutes les colonnes instables vers les colonnes voisines (elle modifie
    donc la liste 'montagne'). La montagne est supposee etre adossee a un
    mur a gauche, mais etre au bord d'un abysse a droite. La fonction renvoie
    le nombre de blocs qui tomberait dans l'abysse au cours de l'experience.
    Exemples:
    >>> montagne = [6,6,5,2,1]
    >>> relaxation(montagne)
    0
    >>> montagne
    [6, 6, 3, 4, 1]

    >>> montagne = [6,4,5,2,3]
    >>> relaxation(montagne)
    2
    >>> montagne
    [6, 4, 3, 4, 1]
    '''

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_relaxation_simple')

# ***************************************************************************
# Badaboummmmmmmmmmmmmmmmmmmmmmmmm...
# ***************************************************************************

def relaxation_totale(montagne):
    '''Prend une montagne instable en entree et procede a toutes les
    relaxations necessaires tant que la montagne n'est pas devenue stable.
    Elle modifie la liste 'montagne' et renvoie le nombre total de blocs
    tombes lors du processus.
    Exemple:
    >>> montagne = [6,6,5,2,1]
    >>> relaxation_totale(montagne)
    4
    >>> montagne
    [6, 4, 3, 2, 1]'''

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_relaxation_totale')



# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
