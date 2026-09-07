SELECT categorie, COUNT(categorie) AS total_produit 
FROM produit
GROUP BY categorie
ORDER BY total_produit ASC;