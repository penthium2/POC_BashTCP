#!/bin/bash
SERVER='localhost'
PORT='6666'
INTERVAL='2'
CHATLOG='log'
echo "" > $CHATLOG
#Fonction qui regard si il y a la question, et réponds "oui" si elle est présente
funk_reponse() {
	if [[ "$1" = "bonjour ça va?" ]] ; then
		printf "Oui"
	fi
}
#cette fonction regarde le contenu de la dernière ligne du fichier de log en continue
funk_input() {
	while true ; do
		#Si le fichier de log a une ligne avec FLAG ou Nope il stop la fonction
		if grep -qs -E 'FLAG|Nope' $CHATLOG ; then
			break
		fi
		#lance la fonction réponse en lui donnant en argument la dernière ligne du fichier log
		funk_reponse "$(tail -1 $CHATLOG)"
		#une tempo, prendre son temps permet d'etre sur d'avoir récup la suite du serveur
		sleep 0.2
	
	done
}
#cette fonction initialise la connexion avec le serveur en lanceant la fonction "input"
funk_start() {
	funk_input | nc -i $INTERVAL $SERVER $PORT > $CHATLOG 2> /dev/null
}
funk_start
sed -n -E 's/^.*(FLAG.*)$/\1/p' $CHATLOG
