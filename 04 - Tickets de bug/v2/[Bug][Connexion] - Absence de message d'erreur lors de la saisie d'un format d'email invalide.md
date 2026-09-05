Priorité : Low
Description

🐛 DESCRIPTION DU BUG
Le système de connexion n'applique aucune vérification de format sur le champ e-mail lors de la soumission du formulaire, permettant l'envoi de données invalides.

👣 ÉTAPES DE REPRODUCTION
Cliquer sur le bouton "Se connecter" ou "S'inscrire / Se connecter" en haut à droite.

Saisir "Adresse mail @@yahoo.fr" dans le champ "Nom d'utilisateur ou e-mail".

Saisir "AZERty12" dans le champ "Mot de passe".

Cliquer sur le bouton "Se connecter" pour valider le formulaire.

❌ COMPORTEMENT ACTUEL (Le Bug)
Aucun message d'erreur de format ne bloque l'utilisateur. Le formulaire tente d'envoyer la requête au serveur avec une adresse e-mail syntaxiquement fausse.

🎯 COMPORTEMENT ATTENDU
L'utilisateur ne doit pas pouvoir soumettre le formulaire.

Un message d'erreur de format doit s'afficher immédiatement sous le champ (ex: "Saisissez une adresse e-mail valide").

Le champ "Nom d'utilisateur ou e-mail" doit être surligné en rouge pour indiquer l'erreur visuellement.

💻 ENVIRONNEMENT DE TEST
OS : Windows 11 

Navigateur : Chrome (Dernière version)