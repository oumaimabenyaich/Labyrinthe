def moveAEnvoyer(tile, gate, new_positions):
    print("generation du move")
    retour = {"tile": "tile" ,"gate": "A","new_position": 0}
    retour["tile"] = tile
    retour["gate"] = gate
    retour["new_position"] = new_positions
    print(retour)
    return retour

def afficherEtat(jsonSS):
    print("les joueurs sont : ", jsonSS["players"])
    print("vous etes le joueur : ", jsonSS["current"] + 1)
    print("votre positions est : " , jsonSS["positions"])
    print("voici le tresor que vous devez attrapper : " , jsonSS["target"])
    print("voici le nombre de tresors manquants" , jsonSS["remaining"])
    print("voici la piece manquante : ")
    if jsonSS["tile"]["N"]:
        print("--        --")
        print("|          |")
    else:
        print("------------")
        print("|          |")
    if jsonSS["tile"]["E"] and jsonSS["tile"]["W"]:
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
        print("            ")
    elif jsonSS["tile"]["E"] == False and jsonSS["tile"]["W"]:
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
    elif jsonSS["tile"]["W"] == False and jsonSS["tile"]["E"]:
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    else: 
        print("|          |")
        print("|          |")
        print("|          |")
        print("|          |")
        print("|          |")
        print("|          |")
    if jsonSS["tile"]["S"]:
        print("|          |")
        print("--        --")
    else:
        print("|          |")
        print("------------")


 #le i sert comme indice pour tester notre code, a partir du 50eme coup, le code va commencer a generer des erreur
 #le state est l'etat du jeu qui sera un dictionnaire
 #la fonction retournera un tuple qui va ensuite etre utiliser par la fonction moveAEnvoyer
def jeuDuCoupTest(i = 0, state = {"a":"b"}):
    print(type(state))
    ################ ici il y aura le code de "l'ia"
    #afficherEtat(jsonS)
    #print("votre piece ne sera pas orientable pace que vazy gros assahbe")
    #porte = input("entree la porte ou vous voulez jouez(une lettre de A à L et en majuscule svp) : ")
    #posFinal = int(input("entree la position ou vous voulez atterir avec votre pion : "))
    porte = "A"
    posFinal = state["positions"][state["current"]]
    tile = state["tile"]
    if i > 50 : 
        posFinal = posFinal + 1
    
    #################### apres sa il s'agit que de l'envoie de la reponse oslm
    return tile , porte , posFinal

#cette fonction va nous retourner un nombre qui va nous servir a comparer et manipuler les tiles entre eux
#un tile ressemble a sa : tile = { "N": true, "E": false, "S": true, "W": true, "item": 1}
def typeTile(tile = {"a":"b"}):
    retour = 0 # un retour = 0 signifiera qu on a une erreur
    #un retour = 1 signifiera qu on a un tile en forme de coude
    #un retour = 2 signifiera qu on a un tile en forme de tube
    #un retour = 3 signifiera qu on a un tile en forme de "T"
    if tile['N'] == False and tile['E'] == True and tile['S'] == False and tile['W'] == True:
        retour = 2
    elif tile['N'] == True and tile['E'] == False and tile['S'] == True and tile['W'] == False:
        retour = 2
    elif tile['N'] == False and tile['E'] == True and tile['S'] == True and tile['W'] == False:
        retour = 1
    elif tile['N'] == False and tile['E'] == False and tile['S'] == True and tile['W'] == True:
        retour = 1
    elif tile['N'] == True and tile['E'] == False and tile['S'] == False and tile['W'] == True:
        retour = 1
    elif tile['N'] == True and tile['E'] == True and tile['S'] == False and tile['W'] == False:
        retour = 1
    elif tile['N'] == True and tile['E'] == True and tile['S'] == False and tile['W'] == True:
        retour = 3
    elif tile['N'] == True and tile['E'] == False and tile['S'] == True and tile['W'] == True:
        retour = 3
    elif tile['N'] == False and tile['E'] == True and tile['S'] == True and tile['W'] == True:
        retour = 3
    elif tile['N'] == True and tile['E'] == True and tile['S'] == True and tile['W'] == False:
        retour = 3

    return retour

#def trouverDesChemin

#retourne la porte ou il y a un pion si elle est au bord sinon retourne "M"
def pionAUnePorte(positionPion = 0):
    retour = "M"
    tableAnalyse = [[1,"A","I"],[3,"B","H"],[5,"C","G"],[13,"D","L"],[27,"E","K"],[41,"F","J"],[47,"G","C"],[45,"H","B"],[43,"I","A"],[35,"J","F"],[21,"K","E"],[7,"L","D"]]
    for i in tableAnalyse:
        if i[0] == positionPion:
            retour = (i[1],i[2])
            break
    return retour

#cette fonction recreer la map sachant que on pousse tt une ligne a travers un couloir et que si un pion se trouve sur un bout 
# de labyrinthe et qu il se retrouve ejecter, alors le joueur réaparait sur la tuile qui vient d 'etre placé 
def recreerLaMap(board = [{"a":"b"}], tile = {"a":"b"}, porte = "A", positionPion = -1):
    carte = board
    tableAnalyse = {"A": [[43,36,29,22,15,8,1],"I"], 
                    "B": [[45,38,31,24,17,10,3],"H"], 
                    "C": [[47,40,33,26,19,12,5],"G"], 
                    "D": [[7,8,9,10,11,12,13],"L"], 
                    "E": [[21,22,23,24,25,26,27],"K"], 
                    "F": [[35,36,37,38,39,40,41],"J"], 
                    "G": [[5,12,19,26,33,40,47],"C"], 
                    "H": [[3,10,17,24,31,38,45],"B"], 
                    "I": [[1,8,15,22,29,36,43],"A"], 
                    "J": [[41,40,39,38,37,36,35],"F"], 
                    "K": [[27,26,25,24,23,22,21],"E"], 
                    "L": [[13,12,11,10,9,8,7],"D"]}
    table = tableAnalyse[porte]
    i=0
    pion = positionPion
    while i<6:
        carte[table[0][i]] = carte[table[0][i+1]]
        i=i+1
    i = 1
    if pionAUnePorte(positionPion) == (table[1],porte):
        pion = table[0][6]
        i = 7
    while i < 7:
        if positionPion == table[0][i]:
            pion = table[0][i-1]
            break
        i = i+1
    carte[table[0][6]] = tile
    retour = (carte,pion)
    return retour

#def genererLesPortesAEssayer()

#retourne l index de la tuile contenant le trésor
def ouEstLeTresor(board = [{"a":"b"}], cible = 0):
    retour = 0
    erreur = True
    for i in board:
        if cible == i["item"]:
            erreur = False
            break
        retour = retour + 1
    if erreur:
        retour = -1
    return retour

def jeuDuCoup(i = 0, state = {"a":"b"}):
    print(type(state))
    ################ ici il y aura le code de "l'ia"
    #afficherEtat(jsonS)
    #print("votre piece ne sera pas orientable pace que vazy gros assahbe")
    #porte = input("entree la porte ou vous voulez jouez(une lettre de A à L et en majuscule svp) : ")
    #posFinal = int(input("entree la position ou vous voulez atterir avec votre pion : "))
    porte = "A"
    posFinal = state["positions"][state["current"]]
    tile = state["tile"]
    if i > 50 : 
        posFinal = posFinal + 1
    
    #################### apres sa il s'agit que de l'envoie de la reponse oslm
    return tile , porte , posFinal
