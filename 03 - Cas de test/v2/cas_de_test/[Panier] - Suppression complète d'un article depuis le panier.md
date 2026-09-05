Priorité : Medium
Description

📋 INFORMATIONS GÉNÉRALES
ID du Cas de Test : CT-PAN-003

Objectif : Vérifier que l'utilisateur peut supprimer avec succès un article de son panier.

⚙️ PRÉREQUIS
L'utilisateur est connecté à son compte.

L'utilisateur possède au moins un article dans son panier.

👣 ÉTAPES DE REPRODUCTION
Cliquer sur l'icône "Panier" en haut à droite (qui indique le nombre d'articles en rouge).

Cliquer sur le bouton "Supprimer" (ou l'icône de poubelle) associé à l'article à retirer.

🎯 RÉSULTAT ATTENDU
L'utilisateur reste sur la page du panier.

L'article est retiré de la liste et un message de confirmation s'affiche (ex : "L'article a été supprimé de ton panier").

Le montant total du panier est mis à jour (le prix de l'article supprimé est déduit).

Le compteur rouge sur l'icône du panier diminue de 1.

Note : Si c'était le seul article présent, le panier affiche désormais le message "Votre panier est vide".

💻 ENVIRONNEMENT DE TEST
OS : Windows 11 

Navigateur : Chrome (Dernière version)