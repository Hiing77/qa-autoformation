SELECT categorie, SUM(quantite) AS quantite_total
FROM produit
WHERE categorie LIKE 'A%' 
GROUP BY categorie
HAVING SUM(quantite) > 5;
