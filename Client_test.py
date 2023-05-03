import socket
import time
import json



def jeuDuCoup(client = socket.socket(), state = """{"a":"b"}"""):
    print("sa joue")



s = socket.socket()
adresse = ("127.0.0.1",3000) #METTRE L'IP et le canal
s.connect(adresse)
requete = """{"request" : "subscribe", "port" : 5000, "name" : "AzizxAisha", "matricules" : ["22375", "21237"]}""".encode()
s.send(requete)
t = socket.socket()
adresse1 = ("0.0.0.0", 5000)
t.bind(adresse1)

donnee = """ { "response" : "lol" } """
donneeStockage = """ { "response" : "lol" } """
while True:
    if donneeStockage == """ { "response" : "lol" } """:
        donnee = s.recv(2048).decode()
        jsonrep = json.loads(donnee)
        if jsonrep["response"] == "error" : # en cas d'erreur
            print("error")
            break
        else: 
            print("ok")
            donneeStockage = donnee
    else:
        t.listen()
        jsonrep = json.loads(donnee)
        if jsonrep["response"] == "ok":
            time.sleep(1)
            clientServeur,adresseServeur = t.accept() #clientServeur est un socket
            messageServeur = clientServeur.recv(2048).decode()
        jsonrepS = json.loads(messageServeur)
        if jsonrepS["request"] == "ping" and jsonrep["response"] != "go":
            clientServeur.send("""{"response" : "pong"}""".encode())
            donnee = """ { "response" : "go" } """
        else:
            print("go jouer")
            #time.sleep(1)
            #clientServeur,adresseServeur = t.accept() #clientServeur est un socket
            #messageServeur = clientServeur.recv(2048).decode()
            if jsonrepS["lives"] == 0:
                clientServeur.send("""{"response": "giveup",}""".encode())
                break
            elif jsonrepS["request"] == "play":
                jeuDuCoup(clientServeur, jsonrepS["state"])
            else: 
                break
    
print("fin")

    

s.close()
t.close()
