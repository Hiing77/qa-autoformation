Priorité : High
Description

🐛 DESCRIPTION DU BUG
Le montant total du panier ne s'actualise pas après la suppression d'un article de la liste.

👣 ÉTAPES DE REPRODUCTION
Cliquer sur l'icône "Panier" en haut à droite (qui indique le nombre d'articles en rouge).

Cliquer sur le bouton "Supprimer" (ou l'icône de poubelle) associé à l'article à retirer.

❌ COMPORTEMENT ACTUEL (Le Bug)
L'utilisateur possède deux articles dans son panier (un à 10€ et un à 20€, total = 30€). Lors de la suppression de l'article à 10€, celui-ci disparaît bien visuellement de la liste, mais le prix total affiché en bas du panier reste bloqué à 30€ au lieu de passer à 20€.

🎯 COMPORTEMENT ATTENDU
L'utilisateur reste sur la page du panier.

L'article est retiré de la liste et un message de confirmation s'affiche (ex : "L'article a été supprimé de votre panier").

Le montant total du panier est mis à jour instantanément (le prix de l'article supprimé est déduit).

Le compteur rouge sur l'icône du panier diminue de 1.

Note : Si c'était le seul article présent, le panier affiche désormais le message "Votre panier est vide".

💻 ENVIRONNEMENT DE TEST
OS : Windows 11

Navigateur : Chrome (Dernière version)