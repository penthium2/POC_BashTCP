#!/usr/bin/env python
import socket

def main():
    host = '127.0.0.1'  # Adresse IP locale
    port = 6666

    # Créer un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lier le socket à l'adresse et au port spécifiés
    server_socket.bind((host, port))

    # Écouter les connexions entrantes
    server_socket.listen(1)
    print(f"Le serveur écoute sur le port {port}...")

    while True:
        # Accepter la connexion du client
        client_socket, client_address = server_socket.accept()
        print(f"Connexion établie avec {client_address}")

        # Envoyer la question au client
        client_socket.sendall("bonjour ça va?\n".encode('utf-8'))

        # Recevoir la réponse du client
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Réponse du client : {response}")

        # Vérifier la réponse et envoyer le message approprié
        if response.lower() == "oui":
            client_socket.sendall("Bravo voici un cadeau FLAG{B4sh_TCP}\n".encode('utf-8'))
        else:
            client_socket.sendall("Nope. Aurevoir.\n".encode('utf-8'))

        # Fermer la connexion avec le client
        client_socket.close()

if __name__ == "__main__":
    main()

