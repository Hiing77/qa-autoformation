Priorité : Medium
Description

📋 INFORMATIONS GÉNÉRALES
ID du Cas de Test : CT-CONN-003

Objectif : Vérifier l'impossibilité de se connecter avec une adresse mail inexistante.

⚙️ PRÉREQUIS
L'adresse mail utilisée est inexistante dans les comptes enregistrés sur Vinted.

L'utilisateur n'est pas connecté.

L'utilisateur se trouve sur la page d'accueil de Vinted.

👣 ÉTAPES DE REPRODUCTION
Cliquer sur le bouton "Se connecter" ou "S'inscrire / Se connecter" en haut à droite.

Saisir une adresse email inexistante dans le champ "Nom d'utilisateur ou e-mail".

Saisir "AZERty12" dans le champ "Mot de passe".

Cliquer sur le bouton "Se connecter" pour valider le formulaire.

🎯 RÉSULTAT ATTENDU
L'utilisateur n'est pas connecté.

Un message d'erreur explicite s'affiche (ex: "Nom d'utilisateur ou mot de passe incorrect").

Le champ "Nom d'utilisateur ou e-mail" reste pré-rempli, tandis que le champ "Mot de passe" est vidé et surligné en rouge.

💻 ENVIRONNEMENT DE TEST
OS : Windows 11 

Navigateur : Chrome (Dernière version)