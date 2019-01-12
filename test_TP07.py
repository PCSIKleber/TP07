from test_TP07z import *


##################################
## Procédure d'exécution des tests
##################################

DICO = {'01_neige': NeigeTest,
    	'02_est_instable': InstableTest,
    	'03_relaxation_simple': RelaxationSimpleTest,
    	'04_relaxation_totale': RelaxationTotaleTest,
        }

def fais_tests(choix):
    '''Fonction qui appelle les batteries de test selon le choix de
    l'utilisateur.'''
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(DICO[choix])
    except:
        print('='*70)
        print('Le choix "%s" ne fait pas partie des possibilites suivantes:' % choix)
        s = '\n  * '
        print(s[1:] + s.join(sorted(list(DICO.keys()))))
        print('='*70)
        exit()
    unittest.TextTestRunner(verbosity=2).run(suite)

def detaille_note():
    '''Pour calculer les notes à chaque sous-suite de tests.'''
    total_general  = 5
    success_general= 0
    for k in sorted(DICO.keys()):
        s = unittest.TestLoader().loadTestsFromTestCase(DICO[k])
        f = open('erreurs.txt','w')
        res = unittest.TextTestRunner(stream=f,verbosity=1).run(s)
        f.close()
        total = res.testsRun
        failed= len(res.failures)
        errors= len(res.errors)
        success = total - failed - errors
        print("{}/{}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
    print('A noter que 5 points seront evalues "a l\'oeil" d\'apres le graphique produit')
