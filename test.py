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


def jeuDuCoup(client = socket.socket(), state = """{"a":"b"}"""):
    print(type(client))
    print(type(state))
    jsonS= json.loads(state)
    ################ ici il y aura le code de "l'ia"
    afficherEtat(jsonS)
    print("votre piece ne sera pas orientable pace que vazy gros assahbe")
    porte = input("entree la porte ou vous voulez jouez(une lettre de A à L et en majuscule svp) : ")
    posFinal = int(input("entree la position ou vous voulez atterir avec votre pion : "))
    #################### apres sa il s'agit que de l'envoie de la reponse oslm
    reponse = """{"response": "move","move": the_move_played,"message": "coup jouer"}"""
    jsonMove = json.loads(reponse)
    jsonMove["move"] = moveAEnvoyer(jsonS["tile"], porte, posFinal)
    reponse = json.dumps(jsonMove)
    client.send(reponse.encode())