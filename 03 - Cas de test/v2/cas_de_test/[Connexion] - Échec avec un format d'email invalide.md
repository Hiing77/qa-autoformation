Priorité : Medium
Description

📋 INFORMATIONS GÉNÉRALES
ID du Cas de Test : CT-CONN-004

Objectif : Vérifier l'impossibilité de se connecter avec un format d'adresse e-mail invalide.

⚙️ PRÉREQUIS
L'utilisateur n'est pas connecté.

L'utilisateur se trouve sur la page d'accueil de Vinted.

👣 ÉTAPES DE REPRODUCTION
Cliquer sur le bouton "Se connecter" ou "S'inscrire / Se connecter" en haut à droite.

Saisir "Adresse mail @@yahoo.fr" dans le champ "Nom d'utilisateur ou e-mail".

Saisir "AZERty12" dans le champ "Mot de passe".

Cliquer sur le bouton "Se connecter" pour valider le formulaire.

🎯 RÉSULTAT ATTENDU
L'utilisateur n'est pas connecté.

Un message d'erreur de format s'affiche (ex: "Saisissez une adresse e-mail valide").

Le champ "Nom d'utilisateur ou e-mail" reste saisi avec la valeur erronée et est surligné en rouge pour indiquer l'erreur.

💻 ENVIRONNEMENT DE TEST
OS : Windows 11 

Navigateur : Chrome (Dernière version)