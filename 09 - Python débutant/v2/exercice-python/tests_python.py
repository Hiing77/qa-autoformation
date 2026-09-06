# --- 1. La Fonction à tester ---
def verifier_mot_de_passe(mdp: str) -> bool:
    """Vérifie si le mot de passe fait au moins 8 caractères et contient un chiffre."""
    if len(mdp) < 8:
        return False

    contient_chiffre = False
    for char in mdp:
        if char.isdigit():
            contient_chiffre = True
            break

    return contient_chiffre


# --- 2. Jeux de données de test (Liste de Dictionnaires) ---
campagne_de_tests = [
    {"input": "Secret123", "attendu": True, "description": "Mot de passe valide"},
    {"input": "Pass123", "attendu": False, "description": "Trop court (7 chars)"},
    {"input": "MotDePasse", "attendu": False, "description": "Sans chiffre"},
    {"input": "", "attendu": False, "description": "Chaîne vide"},
]

# --- 3. Exécution des tests manuels ---
print("=== DÉBUT DU RUN DE TEST ===")

for test in campagne_de_tests:
    resultat = verifier_mot_de_passe(test["input"])

    # Assertion : lève une erreur de type AssertionError si la condition est Fausse
    assert resultat == test["attendu"], (
        f"ÉCHEC sur : {test['description']} "
        f"(Obtenu: {resultat}, Attendu: {test['attendu']})"
    )

    print(f"✅ PASS : {test['description']}")

print("=== TOUS LES TESTS SONT AU VERT ===")
