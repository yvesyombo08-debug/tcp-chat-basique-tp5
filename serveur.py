import socket
from tracemalloc import stop

def demarrer_serveur():
    # 1. Création du socket (IPv4, protocole TCP)
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Définition de l'adresse et du port d'écoute
    host = '127.0.0.1' # Localhost (la machine elle-même)
    port = 9999
    
    # 2. Liaison (Bind) du socket à l'IP et au port
    serveur_socket.bind((host, port))
    
    # 3. Écoute des connexions entrantes (1 client max en file d'attente)
    serveur_socket.listen(1)
    print(f"[*] Le serveur écoute sur {host}:{port}...")
    
    # 4. Acceptation de la connexion du client
    client_socket, client_address = serveur_socket.accept()
    print(f"[+] Connexion acceptée depuis {client_address[0]}:{client_address[1]}")
    
    while True:
    
        donnees_recues = client_socket.recv(1024).decode('utf-8')
        if donnees_recues.strip().lower() =="stop":
            print("Arrêt")
            break

        # 5. Réception des données (1024 octets max)
        print(f"[>] Message du client : {donnees_recues}")
        break
    
        # 6. Réponse au client
        reponse = "Hello Client ! Message bien reçu, fin de transmission."
        client_socket.send(reponse.encode('utf-8'))

        # 7. Fermeture propre des sockets
        client_socket.close() 
        serveur_socket.close()
        print("[*] Serveur éteint.")

if __name__ == "__main__":
    demarrer_serveur()