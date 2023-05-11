board1 = [{"N": False, "E": True, "S": True, "W": False, "item": None}, #0
         {"N": False, "E": True, "S": False, "W": True, "item": 0}, #1
         {"N": False, "E": True, "S": True, "W": True, "item": None}, #2
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #3
         {"N": False, "E": True, "S": True, "W": True, "item": 1}, #4
         {"N": False, "E": False, "S": True, "W": True, "item": 15}, #5
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #6
         {"N": True, "E": True, "S": False, "W": False, "item": 12}, #7
         {"N": True, "E": False, "S": True, "W": True, "item": 19}, #8
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #9 
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #10
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #11
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #12
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #13
         {"N": True, "E": True, "S": True, "W": False, "item": 2}, #14
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #15
         {"N": True, "E": True, "S": True, "W": False, "item": 3}, #16
         {"N": True, "E": True, "S": True, "W": False, "item": 20}, #17
         {"N": False, "E": True, "S": True, "W": True, "item": 4}, #18
         {"N": True, "E": True, "S": True, "W": False, "item": 23}, #19
         {"N": True, "E": False, "S": True, "W": True, "item": 5}, #20
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #21
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #22
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #23
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #24
         {"N": False, "E": True, "S": True, "W": False, "item": 14}, #25
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #26
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #27
         {"N": True, "E": True, "S": True, "W": False, "item": 6}, #28
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #29
         {"N": True, "E": True, "S": False, "W": True, "item": 7}, #30
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #31
         {"N": True, "E": False, "S": True, "W": True, "item": 8}, #32
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #33
         {"N": True, "E": False, "S": True, "W": True, "item": 9}, #34
         {"N": True, "E": True, "S": False, "W": False, "item": 13}, #35
         {"N": True, "E": True, "S": False, "W": True, "item": 21}, #36
         {"N": True, "E": True, "S": False, "W": True, "item": 18}, #37
         {"N": True, "E": False, "S": False, "W": True, "item": 17}, #38
         {"N": False, "E": True, "S": True, "W": True, "item": 22}, #39
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #40
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #41
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #42
         {"N": False, "E": True, "S": False, "W": True, "item": 10}, #43
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': None}, #44
         {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, #45
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, #46
         {'N': False, 'E': True, 'S': True, 'W': False, 'item': 16},   #47 ######################
         {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}] #48
tileH = {"N": False, "E": True, "S": True, "W": False, "item": None}


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


board = [{"N": False, "E": True, "S": True, "W": False, "item": None}, #0
         {"N": False, "E": True, "S": False, "W": True, "item": 0}, #1
         {"N": False, "E": True, "S": True, "W": True, "item": None}, #2
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #3
         {"N": False, "E": True, "S": True, "W": True, "item": 1}, #4
         {"N": False, "E": False, "S": True, "W": True, "item": 15}, #5
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #6
         {"N": True, "E": True, "S": False, "W": False, "item": 12}, #7
         {"N": True, "E": False, "S": True, "W": True, "item": 19}, #8
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #9 
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #10
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #11
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #12
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #13
         {"N": True, "E": True, "S": True, "W": False, "item": 2}, #14
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #15
         {"N": True, "E": True, "S": True, "W": False, "item": 3}, #16
         {"N": True, "E": True, "S": True, "W": False, "item": 20}, #17
         {"N": False, "E": True, "S": True, "W": True, "item": 4}, #18
         {"N": True, "E": True, "S": True, "W": False, "item": 23}, #19
         {"N": True, "E": False, "S": True, "W": True, "item": 5}, #20
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #21
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #22
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #23
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #24
         {"N": False, "E": True, "S": True, "W": False, "item": 14}, #25
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #26
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #27
         {"N": True, "E": True, "S": True, "W": False, "item": 6}, #28
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #29
         {"N": True, "E": True, "S": False, "W": True, "item": 7}, #30
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #31
         {"N": True, "E": False, "S": True, "W": True, "item": 8}, #32
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #33
         {"N": True, "E": False, "S": True, "W": True, "item": 9}, #34
         {"N": True, "E": True, "S": False, "W": False, "item": 13}, #35
         {"N": True, "E": True, "S": False, "W": True, "item": 21}, #36
         {"N": True, "E": True, "S": False, "W": True, "item": 18}, #37
         {"N": True, "E": False, "S": False, "W": True, "item": 17}, #38
         {"N": False, "E": True, "S": True, "W": True, "item": 22}, #39
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #40
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #41
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #42
         {"N": False, "E": True, "S": False, "W": True, "item": 10}, #43
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': None}, #44
         {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, #45
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, #46
         {'N': False, 'E': True, 'S': True, 'W': False, 'item': 16},   #47 ######################
         {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}] #48

tileH = {"N": False, "E": True, "S": True, "W": False, "item": None}
porteH = "A"
pos = 43
afficherLePlateau(board, tileH, pos)
print(' ')
boardR, newPion = recreerLaMap(board, tileH, "A", pos)
afficherLePlateau(boardR, tileH, newPion)
tresor = 10
print(boardR) 