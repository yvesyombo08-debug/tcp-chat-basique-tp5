from os import link
import socket

def demarrer_client():
    # 1. Création du socket client (IPv4, TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # L'adresse et le port du serveur que l'on veut joindre
    host = '127.0.0.1'
    port = 9999
    
    try:
        # 2. Tentative de connexion au serveur
        print(f"[*] Tentative de connexion à {host}:{port}...")
        client_socket.connect((host, port))
        print("[+] Connecté au serveur !")
        
        while True:
            reponse = input("Tapez 'link' pour envoyer le messagee :")
            if reponse == "link":
                # 3. Envoi du message initial
                message = "Hello Serveur"
                client_socket.send(message.encode('utf-8'))
                print(f"[<] Message envoyé : '{message}'")
        
                # 4. Réception de la réponse du serveur
                reponse = client_socket.recv(1024).decode('utf-8')
                print(f"[<] Réponse du serveur : {reponse}")
    
            else:
                message = "Stop"
                client_socket.send(message.encode('utf-8'))
                print("Communication arrêté")
                break

    except ConnectionRefusedError:
        print("[-] Erreur : Le serveur est introuvable. Est-il bien lancé ?")

    finally:
        # 5. Fermeture de la connexion
        client_socket.close()
        print("[*] Connexion fermée.")

if __name__ == "__main__":
    demarrer_client()