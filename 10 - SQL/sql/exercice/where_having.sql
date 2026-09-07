SELECT categorie, SUM(quantite) AS total_quantité
FROM produit 
WHERE quantite > 3 
GROUP BY categorie 
HAVING SUM(quantite) > 10;