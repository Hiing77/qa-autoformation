Scénario 1 : Connexion utilisateur 🔐

email_correct = "user@test.com"
mot_de_passe_correct = "12345"

FUNCTION connecter_utilisateur(email_saisi, mot_de_passe_saisi)

IF email_saisi = email_correct AND mot_de_passe_saisi = mot_de_passe_correct THEN
DISPLAY "Connexion réussie !"

ELSE
DISPLAY "Identifiants incorrects."

ENDIF
ENDFUNCTION

connecter_utilisateur ("user@test.com", "12345")

______________________________________________________________
Scénario 2 : Validation de champ (Email vide) 📧

FUNCTION valider_champ_email(email)

IF email = "" THEN
DISPLAY "Erreur : L'adresse email ne peut pas être vide !"

ELSE
DISPLAY "Adresse email valide !"

ENDIF
ENDFUNCTION

valider_champ_email("")

valider_champ_email("user@test.com")

______________________________________________________________
Scénario 3 : Parcours d'un formulaire 📋

FUNCTION valider_formulaire(email, mot_de_passe)

IF email = "" OR mot_de_passe = "" THEN
DISPLAY "Erreur : Tous les champs doivent être remplis !"

ELSE
DISPLAY "Formulaire valide !"

ENDIF
ENDFUNCTION

valider_formulaire("", "12345")

valider_formulaire("user@test.com", "12345")

______________________________________________________________
Scénario 4 : Vérification d'une liste d'emails 📧

FUNCTION verifier_liste_emails(liste_emails)

FOR EACH email IN liste_emails DO

IF email = "" THEN
DISPLAY "Alerte : Un email de la liste est vide !"

ENDIF
ENDFOR
ENDFUNCTION

mes_emails = ["user1@test.com", "", "user2@test.com"]

verifier_liste_emails (mes_emails)

______________________________________________________________
Scénario 5 : Compteur d'erreurs dans un formulaire 📊

FUNCTION compter_erreurs(liste_champs)
nombre_erreurs = 0

FOR EACH champ IN liste_champs DO

IF champ = "" THEN
nombre_erreurs = nombre_erreurs + 1

ENDIF
ENDFOR

DISPLAY nombre_erreurs

ENDFUNCTION

champs_formulaire = ["Jean", "", "user@test.com", ""]

compter_erreurs(champs_formulaire)
______________________________________________________________
BONUS Compteur de tests réussis 🧪

FUNCTION compter_tests_reussis(liste_resultats)
succes = 0

FOR EACH resultats IN liste_resultats DO
IF resultats = "OK" THEN
succes = succes + 1

ENDIF
ENDFOR

DISPLAY succes

ENDFUNCTION

mes_tests = ["OK", "KO", "OK", "OK", "KO"]

compter_tests_reussis (mes_tests)
______________________________________________________________
BONUS Compteur de bugs critiques 🐛

FUNCTION compter_bugs_critiques(liste_severites)
bugs_critiques = 0

FOR EACH severites IN liste_severites DO

IF severites = "CRITICAL" THEN
bugs_critiques = bugs_critiques + 1

ENDIF
ENDFOR

DISPLAY bugs_critiques

ENDFUNCTION

rapport_bugs = ["LOW", "CRITICAL", "MEDIUM", "CRITICAL", "LOW"]

compter_bugs_critiques (rapport_bugs)

______________________________________________________________
Compteur d'erreurs HTTP 404 🌐

FUNCTION compter_pages_introuvables(liste_codes_http)
erreurs_404 = 0

FOR EACH http IN liste_codes_http DO

IF http = 404 THEN
erreurs_404 = erreurs_404 + 1

ENDIF
ENDFOR

DISPLAY erreurs_404

ENDFUNCTION

journal_http = [200, 404, 500, 404, 200]

compter_pages_introuvables (journal_http)

