Priorité : Low
Description

📋 INFORMATIONS GÉNÉRALES
ID du Cas de Test : CT-PAN-005

Objectif : Vérifier le comportement du panier et l'impossibilité de commander si un article présent dans le panier a été acheté par un autre utilisateur entre-temps.

⚙️ PRÉREQUIS
L'utilisateur A est connecté à son compte.

L'utilisateur A possède un article unique dans son panier.

Pendant ce temps, un utilisateur B a acheté et payé ce même article (qui est désormais vendu).

👣 ÉTAPES DE REPRODUCTION
Cliquer sur l'icône "Panier" en haut à droite pour ouvrir le panier.

Constater l'état visuel de l'article devenu indisponible.

Tenter de cliquer sur le bouton "Valider le panier" (ou "Passer la commande").

🎯 RÉSULTAT ATTENDU
L'article dans le panier est grisé ou marqué d'une étiquette explicite (ex : "Indisponible" ou "Vendu").

Le bouton "Valider le panier" est soit désactivé (cliquable impossible), soit son clic bloque l'utilisateur et affiche un message d'erreur clair (ex : "Cet article n'est plus disponible, veuillez le retirer de votre panier pour continuer").

L'utilisateur ne peut pas accéder à l'étape du choix de livraison ni du paiement.

💻 ENVIRONNEMENT DE TEST
OS : Windows 11 

Navigateur : Chrome (Dernière version)