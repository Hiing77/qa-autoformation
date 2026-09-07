SELECT categorie, SUM(quantite) AS total_quantite 
FROM produit 
GROUP BY categorie;