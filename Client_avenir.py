import socket
import json
from fonctions import moveAEnvoyer
from fonctions import jeuDuCoup




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