# POC_BashTCP

Voic un petit poc pour montrer comment gérer une connexion TCP avec BASH.

Ce POC contient 2 fichiers :

Le fichier server.py

        le serveur qui simplement pose une question en via tcp et attend comme réponse : "oui"
        Si la réponse est oui alors le serveur donne un FLAG


Le fichier poc.sh

        Script qui va se connecter au serveur et répondre oui puis affichier le FLAG
