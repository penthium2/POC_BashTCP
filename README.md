# POC_BashTCP

Voic un petit poc pour montrer comment gérer une connexion TCP avec BASH.

Ce POC contient 2 fichiers :

Le fichier server.py

        le serveur qui simplement pose une question en via tcp et attend comme réponse : "oui"
        Si la réponse est oui alors le serveur donne un FLAG


Le fichier poc.sh

        Script qui va se connecter au serveur et répondre oui puis affichier le FLAG

Biensur pour des connexions plus complexe ce script devra etre adapté, je pense a des serveur qui envois plusieur ligne des explications, intéragisse plusieurs fois, etc...

Mais là vous avez la base..

la seul limite est qu'il faut nc sur la machine exécutant le script bash, le reste est natif.

Have FUN in BASH !!

\#BASH4EVER