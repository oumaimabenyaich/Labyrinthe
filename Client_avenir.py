import socket
import json
#juste pour commit

def moveAEnvoyer(tile, gate, new_positions):
    print("generation du move")
    retour = {"tile": "tile" ,"gate": "A","new_position": 0}
    retour["tile"] = tile
    retour["gate"] = gate
    retour["new_position"] = new_positions
    print(retour)
    return retour

 #le i sert comme indice pour tester notre code, a partir du 50eme coup, le code va commencer a generer des erreur
 #le state est l'etat du jeu qui sera un dictionnaire
 #la fonction retournera un tuple qui va ensuite etre utiliser par la fonction moveAEnvoyer
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


# on est le client IA
s = socket.socket()
address = ('localhost', 3000)  # port du prof
s.connect(address)
request = {
    "request": "subscribe",
    "port": 5000,     # numero de port choisi par nous
    "name": "Notre Jeu",
    "matricules": ["19516", "19519"]
}
# message qu'on envoie au serveur qui contient les données d'inscription
message = json.dumps(request).encode()
s.send(message)
reponse = s.recv(2048).decode()  # on ecoute la reponse du serveur
print("reponse:", reponse)
s.close()

# les roles s'inversent, on devient le serveur jeu

s = socket.socket()
s.bind(('0.0.0.0', 5000))
s.listen()



o = -1
while True:
    client, address = s.accept()
    with client:
        message = json.loads(client.recv(10000).decode())
        print(message)

        if message == {'request': 'ping'}:
            client.send(json.dumps({'response': 'pong'}).encode())
            print("pong")
# dictionnaire qu on transforme en json avec dumps puis qu on transforme en binaire avec encode pour pouvoire l'envoyer au client

        else:
            # liste pour recuper la clé state du dictionnaire

            print("cest sensé jouer")
            tile, gate, new_positions = jeuDuCoup(o, message["state"])
            o = o +1
            client.send(json.dumps({
                "response": "move",
                "move": moveAEnvoyer(tile, gate, new_positions),
                "message": "let's play"
            }).encode())