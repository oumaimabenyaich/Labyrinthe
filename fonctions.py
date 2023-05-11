def moveAEnvoyer(tile, gate, new_positions):
    print("generation du move")
    retour = {"tile": "tile" ,"gate": "A","new_position": 0}
    retour["tile"] = tile
    retour["gate"] = gate
    retour["new_position"] = new_positions
    print(retour)
    return retour

 #Le i sert d'indice pour tester notre code, à partir du 50eme coup, le code commence à générer des erreurs
 #Le state est l'etat du jeu qui sera un dictionnaire {"players": ["LUR", "HSL"],"current": 0,"positions": [6, 47],"target": 3,"remaining": [4, 4],"tile": <the free tile>,"board": <list of 49 tiles>}
 #La fonction retournera un tuple qui sera ensuite utilisé par la fonction moveAEnvoyer 
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


#Cette fonction va retourner un nombre qui va nous servir à comparer et manipuler les tiles entre eux
#un tile = { "N": true, "E": false, "S": true, "W": true, "item": 1}
def typeTile(tile = {"a":"b"}):
    retour = 0 
    #Retour = 0 signifie qu'on a une erreur
    #Retour = 1 signifie qu'on a un tile en forme de coude
    #Retour = 2 signifie qu'on a un tile en forme de tube
    #Retour = 3 signifie qu'on a un tile en forme de "T"
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

#cette fonction nous permettra de savoir si on peut encore avancer dans une ou plusieurs direction ou si on est dans un cul de sac
#cette fonction retourne un tuple contenant la case actuel , le nombre de case possible et une liste contenant les tuiles ou on
#peut avancer (ex: (42,1,[35]))   tuileA = {"N": False} , tuileN = {"N": False} , tuileE = {"N": False} , tuileS = {"N": False} , tuileW = {"N": False}
def yAQuoiCommePossiblite(positionActuelle = 0 , parent = 0 , board = [{"a":"b"}] ):
    retourPossibilite = []
    retourNombre = 0
    x = positionActuelle % 7
    y = (positionActuelle - x) / 7

    if y != 0:
        if board[positionActuelle-7]["S"] == board[positionActuelle]["N"] == True:
            if (positionActuelle - 7) != parent:
                retourNombre = retourNombre +1
                retourPossibilite.append(positionActuelle - 7)
    if x != 6:
        if board[positionActuelle+1]["W"] == board[positionActuelle]["E"] == True:
            if (positionActuelle +1) != parent:
                retourNombre = retourNombre +1
                retourPossibilite.append(positionActuelle+1)
    if y != 6:
        if board[positionActuelle+7]["N"] == board[positionActuelle]["S"] == True:
            if (positionActuelle +7) != parent:
                retourNombre = retourNombre +1
                retourPossibilite.append(positionActuelle+7)
    if x != 0:
        if board[positionActuelle-1]["E"] == board[positionActuelle]["W"] == True:
            if (positionActuelle -1) != parent:
                retourNombre = retourNombre +1
                retourPossibilite.append(positionActuelle-1)
    return [positionActuelle , retourNombre , retourPossibilite ]

#cette fonction permet de remonter le chemin parcouru jusqu a un carrefour
#on lui envoie une queu contenant toute les case parcouru et le noeud ou l on souhaite reprendre son chemin
def remonterAuNoeud(queu = [], noeud = 0):
    retour = [0]
    cheminAnePasEssayer = 0
    i = 1
    while i <= queu[0]:
        if queu[i] == noeud:
            retour[0] = retour[0] + 1
            retour.append(queu[i])
            cheminAnePasEssayer = queu[i+1]
            break
        else:
            retour[0] = retour[0] + 1
            retour.append(queu[i])
        i = i + 1
    return [retour,cheminAnePasEssayer]
        

def trouverDesChemin(board = [{"a":"b"}], positionPion = -1, positionTresor = -1, typeTile = 0,porte = "A"):
        #[positionActuelle , retourNombre , retourPossibilite ]
    bibliPorte = {"A":1 ,"B":3 ,"C":5 ,"D":13 ,"E":27 ,"F":41 ,"G":47 ,"H":45 ,"I":43 ,"J":35 ,"K":21 ,"L":7}
    retour = []
    typeUtile = [-1,-1,-1]
    passageTuile = False
    queu = [1,positionPion]
    tuilePossible = yAQuoiCommePossiblite(queu[queu[0]] , queu[queu[0]] , board)
    if tuilePossible[1] != 0:
        if tuilePossible[1] == 1:
            queu[0] = queu[0] + 1
            queu.append(tuilePossible[2][0])
            if queu[queu[0]] == bibliPorte[porte]:
                passageTuile = True
                typeUtile = [positionPion, queu[queu[0]], -1]
        else:
            queu[0] = queu[0] + 1
            queu.append(tuilePossible[2][0])
            if queu[queu[0]] == bibliPorte[porte]:
                passageTuile = True
                typeUtile = [positionPion, queu[queu[0]], -1]
        if queu[queu[0]] == positionTresor:
            return [positionTresor,typeUtile]
    else: 
        return [positionPion,typeUtile]
    
    while True:
        tuilePossible = yAQuoiCommePossiblite(queu[queu[0]] , queu[queu[0]-1] , board)
        if tuilePossible[1] != 0:
            if tuilePossible[1] == 1:
                queu[0] = queu[0] + 1
                queu.append(tuilePossible[2][0])
                if queu[queu[0]] == bibliPorte[porte]:
                    passageTuile = True
                    typeUtile = [positionPion, queu[queu[0]], -1]
                if passageTuile:
                    typeUtile[2] = queu[queu[0]]
                    passageTuile = False
            else:
                queu[0] = queu[0] + 1
                queu.append(tuilePossible[2][0])
                if queu[queu[0]] == bibliPorte[porte]:
                    passageTuile = True
                    typeUtile = [positionPion, queu[queu[0]], -1]
                if passageTuile:
                    typeUtile[2] = queu[queu[0]]
                    passageTuile = False
            if queu[queu[0]] == positionTresor:
                return [positionTresor,typeUtile]
        else:
            return [queu[queu[0]],typeUtile]
    

#Retourne la porte où il y a un pion si elle est au bord sinon retourne "M"
def pionAUnePorte(positionPion = 0):
    retour = "M"
    tableAnalyse = [[1,"A","I"],[3,"B","H"],[5,"C","G"],[13,"D","L"],[27,"E","K"],[41,"F","J"],[47,"G","C"],[45,"H","B"],[43,"I","A"],[35,"J","F"],[21,"K","E"],[7,"L","D"]]
    for i in tableAnalyse:
        if i[0] == positionPion:
            retour = (i[1],i[2])
            break
    return retour

#Sachant qu'on pousse toute une ligne à travers un couloir et que si un pion se trouve sur un bout de labyrinthe et qu'il se retrouve éjecter, alors le joueur réapparait sur la tuile qui vient d'être placée 
def recreerLaMap(board = [{"a":"b"}], tile = {"a":"b"}, porte = "A", positionPion = -1):
    carte = board.copy()
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


#retourne l'index de la tuile contenant le trésor
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

#Cette fonction génère une liste contenant les portes à essayer. La porte à ne pas essayer ? La porte qui sort la tuile contenant le trésor
def genererLesPortesAEssayer(positionTresor = 0):
    porteABan = pionAUnePorte(positionTresor)
    table = ["A","B","C","D","E","F","G","H","I","J","K","L"]
    if porteABan == "M":
        return table
    retour = []
    for i in table:
        if i != porteABan[1]:
            retour.append(i)
    return retour


#Cette fonction affiche le plateau de jeu, la tuile manquante ainsi que la position du pion
#Cette fonction n'a pour but que de traquer les erreurs
def afficherLePlateau(board = [{"a":"b"}], tile = {"a":"b"}, positionPion = -1):
#Le pion se trouve en :  "
    indexNav = [0,1,2,3,4,5,6]
    indexNavL = [0,1,2,3,4,5]
    ligne = ""
    #Par ligne
    for i in indexNavL:
        for o in indexNav:
            ligne  = ligne + "*"
            if board[(i*7)+o]["N"] == True:
                ligne = ligne + "  * "
            else:
                ligne = ligne + "--* "
        print(ligne)
        ligne = ""
        for o in indexNav:
            if board[(i*7)+o]["W"] == True:
                ligne = ligne + " "
            else:
                ligne = ligne + "|"
            if board[(i*7)+o]["item"] == None:
                ligne = ligne + "  "
            else:
                if board[(i*7)+o]["item"] < 10:
                    ligne = ligne + " "
                    ligne = ligne + str(board[(i*7)+o]["item"])
                else:
                    ligne = ligne + str(board[(i*7)+o]["item"])
            if board[(i*7)+o]["E"] == True:
                ligne = ligne + "  "
            else: 
                ligne = ligne + "| "
        print(ligne)
        ligne = ""
        for o in indexNav:
            ligne  = ligne + "*"
            if board[(i*7)+o]["S"] == True:
                ligne = ligne + "  * "
            else:
                ligne = ligne + "--* "
        print(ligne)
        ligne  = ""
    
    for o in indexNav:
            ligne  = ligne + "*"
            if board[(42)+o]["N"] == True:
                ligne = ligne + "  * "
            else:
                ligne = ligne + "--* "
    ligne  = ligne + "*"
    if tile["N"] == True:
        ligne = ligne + "  * "
    else:
        ligne = ligne + "--* "
    print(ligne)
    ligne = ""
    for o in indexNav:
        if board[(42)+o]["W"] == True:
            ligne = ligne + " "
        else:
            ligne = ligne + "|"
        if board[(42)+o]["item"] == None:
            ligne = ligne + "  "
        else:
            if board[(42)+o]["item"] < 10:
                ligne = ligne + " "
                ligne = ligne + str(board[(42)+o]["item"])
            else:
                ligne = ligne + str(board[(42)+o]["item"])
        if board[(42)+o]["E"] == True:
            ligne = ligne + "  "
        else: 
            ligne = ligne + "| "
    if tile["W"] == True:
        ligne = ligne + " "
    else:
        ligne = ligne + "|"
    if tile["item"] == None:
        ligne = ligne + "  "
    else:
        if tile["item"] < 10:
            ligne = ligne + " "
            ligne = ligne + str(tile["item"])
        else:
            ligne = ligne + str(tile["item"])
    if tile["E"] == True:
        ligne = ligne + "  "
    else: 
        ligne = ligne + "| "
    print(ligne)
    ligne = ""
    for o in indexNav:
        ligne  = ligne + "*"
        if board[(42)+o]["S"] == True:
            ligne = ligne + "  * "
        else:
            ligne = ligne + "--* "
    ligne  = ligne + "*"
    if tile["S"] == True:
        ligne = ligne + "  * "
    else:
        ligne = ligne + "--* "
    ligne = ligne + " Le pion se trouve en : " + str(positionPion)
    print(ligne)
    
def trouverTypeTile(tableTile = [-1,-1,-1], tile = {"N": False}):
    retourTile = {"N": False, "E": False, "S": False, "W": False, "item": None}
    retourTile["item"] = tile["item"]
    if ((tableTile[1] - tableTile[0]) == -1) or ((tableTile[1] - tableTile[2]) == -1):
        retourTile["E"] = True
    if ((tableTile[1] - tableTile[0]) == 1) or ((tableTile[1] - tableTile[2]) == 1):
        retourTile["W"] = True
    if ((tableTile[1] - tableTile[0]) == -7) or ((tableTile[1] - tableTile[2]) == -7):
        retourTile["S"] = True
    if ((tableTile[1] - tableTile[0]) == 7) or ((tableTile[1] - tableTile[2]) == 7):
        retourTile["N"] = True
    return [retourTile, typeTile(retourTile)]

#Retour = 0 signifie qu'on a une erreur
#Retour = 1 signifie qu'on a un tile en forme de coude
#Retour = 2 signifie qu'on a un tile en forme de tube
#Retour = 3 signifie qu'on a un tile en forme de "T"

#porteI porte qu on essaye
#typeTile [tile approximatif, type tile]
#chemin  [positionfinalePion, informationUtilePourTrouverLatileAPlacer [-1,-1,-1] ]
#donneeCruciale = [porteI, chemin, typeTile]

def peutIlEtreJouer(donneeAtrier = [], typeTile = 0):
    if typeTile == 3:
        return donneeAtrier
    retour = []
    for i in donneeAtrier:
        if i[2][1] == typeTile:
            retour.append(i)
    return retour
    

def meuilleurMove():
    print("salut")

def placerTile():
    print("salut")




def jeuDuCoup(i = 0, state = {"a":"b"}):
    print(type(state))
    porte = "A"
    posPionInitiale = state["positions"][state["current"]]
    tile = state["tile"]
    board = state["board"]
    tresor = state["target"]
    porteAessayer = genererLesPortesAEssayer(ouEstLeTresor(board ,tresor))
    typeT = typeTile(tile)
    stockage = []
    for porteI in porteAessayer:
        donneeCruciale = [porteI]
        new_board , posPion = recreerLaMap(board, tile, porteI, posPionInitiale)
        positionTresor = ouEstLeTresor(new_board ,tresor)
        chemin = trouverDesChemin(new_board,posPion, positionTresor, typeT,porteI)
        donneeCruciale.append(chemin)
        typeTile = trouverTypeTile(chemin[1], tile)
        donneeCruciale.append(typeTile)
        stockage.append(donneeCruciale)
    



    #################### apres sa il s'agit que de l'envoie de la reponse oslm
    return tile , porte , posFinal
