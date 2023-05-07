import socket
import json
from fonctions import moveAEnvoyer
from fonctions import jeuDuCoupTest



# on est le client IA
s = socket.socket()
address = ('localhost', 3000)  # port du prof
s.connect(address)
request = {
    "request": "subscribe",
    "port": 8889,     # numero de port choisi par nous
    "name": "Notre Test",
    "matricules": ["19000", "19500"]
}
# message qu'on envoie au serveur qui contient les données d'inscription
message = json.dumps(request).encode()
s.send(message)
reponse = s.recv(10000).decode()  # on ecoute la reponse du serveur
print("reponse:", reponse)
s.close()

# les roles s'inversent, on devient le serveur jeu

s = socket.socket()
s.bind(('0.0.0.0', 8889))
s.listen()

o = -1
while True:
    client, address = s.accept()
    with client:
        messagebis = client.recv(10000).decode()
        print("########################")
        print("avant jsonLoad")
        print(messagebis)
        print(type(messagebis))
        message = json.loads(messagebis)
        print("apres jsonLoad")
        print(message)
        print(type(message))
        print("########################")

        if message == {'request': 'ping'}:
            client.send(json.dumps({'response': 'pong'}).encode())
            print("pong")
# dictionnaire qu on transforme en json avec dumps puis qu on transforme en binaire avec encode pour pouvoire l'envoyer au client

        else:
            # liste pour recuper la clé state du dictionnaire

            print("cest sensé jouer")
            tile, gate, new_positions = jeuDuCoupTest(o, message["state"])
            o = o +1
            client.send(json.dumps({
                "response": "move",
                "move": moveAEnvoyer(tile, gate, new_positions),
                "message": "let's play"
            }).encode())