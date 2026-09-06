<!-- Premier scenario  -->

VARIABLE
Liste [50, 10, 80, 5, 100, 15]
i = 0

WHILE (i < 6 )

IF ( Liste[i] <= 15 )
PRINT "PASSER A LA POMPE"

i= i + 1

<!-- Deuxieme scenario  -->

VARIABLE 
ages [12, 20, 15, 18]
abonnements [1, 1, 0, 1]
compteur_acces = 0
i = 0

WHILE (i < 4)

IF (ages[i] >= 18 AND abonnements[i] == 1)
compteur_acces = compteur_acces + 1

i = i + 1

PRINT "ACCES :" + compteur_acces

<!-- Troisieme scenario  -->

VARIABLE
relevés_BPM [72, 75, 60, 52, 48, 55]
sommeil = 0
i = 0

WHILE (i < 6 )

IF (relevés_BPM[i] < 58 )
sommeil = sommeil + 1

i = i + 1

PRINT "SOMMEIL :" + sommeil

<!-- Quatrieme scenario -->

VARIABLE
Poids_camions [12, 18, 15, 10]
poids_total = 0
i = 0

WHILE ( i < 4 )

poids_total = Poids_camions[i] + poids_total

i = i + 1

PRINT "POIDS TOTAL : " + poids_total

<!-- Quatrieme scenario -->
VARIABLE
Ventes_réalisées [5000, 12000, 8000, 15000, 3000]
nb_bonus = 0
total_argent = 0
i = 0

WHILE ( i < 5)

IF (Ventes_réalisées [i] >= 10000 )
nb_bonus = nb_bonus + 1
total_argent = total_argent + 500

i = i + 1

PRINT "VENDEUR :" + nb_bonus AND "TOTAL" + total_argent


<!-- Cinquieme scenario  -->

VARIABLE
carton [10, 5, 8, 20, 12, 15]
stock_total = 0
i = 0

WHILE ( i < 6 )

stock_total = stock_total + carton[i] + 2

i = i + 1

PRINT "STOCK TOTAL :" + stock_total

<!-- Sixieme scenario -->

VARIABLE
Liste_prix_HT [10, 50, 200]
prix_final = 0
i = 0

WHILE ( i < 3)

IF (Liste_prix_HT[i] < 20)
(prix_final = Liste_prix_HT[i] * 1.10)
PRINT "PRIX FINAL :" + prix_final

ELSE IF (Liste_prix_HT[i] >= 20 AND Liste_prix_HT[i] <= 100)
(prix_final = Liste_prix_HT[i] * 1.20)
PRINT "PRIX FINAL :" + prix_final

ELSE 
(prix_final = Liste_prix_HT[i] * 1.30)
PRINT "PRIX FINAL :" + prix_final

i = i + 1

<!-- Septieme scenario  -->

VARIABLE 
Poids_colis [0.5, 5, 15]
frais_livraison = 0
i = 0

WHILE (i < 3)


IF (Poids_colis[i] < 1)
frais_livraison = 0 
PRINT "PAYER :" + frais_livraison 

ELSE IF (Poids_colis[i] >= 1 AND Poids_colis[i] <= 10)
(frais_livraison = Poids_colis[i]*5)
PRINT "PAYER :" + frais_livraison 

ELSE
(frais_livraison = 60)
PRINT "PAYER :" + frais_livraison 

i= i + 1


<!-- Huitieme scenario -->

VARIABLE
Achats_client [15, 80, 150]
points_gagnés = 0
total_points_fidelite = 0
i=0

WHILE (i < 3)

IF
(Achats_client[i] < 50 )
points_gagnés = Achats_client[i] * 2
total_points_fidelite = total_points_fidelite + points_gagnés
PRINT "POINT GAGNE:" + points_gagnés

ELSE IF (Achats_client[i] >= 50 AND Achats_client[i] <= 100)
points_gagnés = 150
total_points_fidelite = total_points_fidelite + points_gagnés
PRINT "POINT GAGNE:" + points_gagnés

ELSE
points_gagnés = Achats_client[i] * 3
total_points_fidelite = total_points_fidelite + points_gagnés
PRINT "POINT GAGNE:" + points_gagnés

i = i + 1

PRINT "POINT TOTAL:" + total_points_fidelite

<!-- Ecrire du pseudo-code pour une connexion utilisateur. -->

FUNCTION


VARIABLE

IF

ELSE























