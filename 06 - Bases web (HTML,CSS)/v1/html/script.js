// On sélectionne les éléments
const emailField = document.getElementById('emailInput');
const passwordField = document.getElementById('passwordInput');
const loginButton = document.getElementById('loginBtn');
const messageDisplay = document.getElementById('message');

// Vérification de sécurité dans la console du navigateur
console.log("Bouton trouvé :", loginButton);

if (loginButton) {
    loginButton.addEventListener('click', function(event) {
        event.preventDefault(); // Bloque le rechargement
        
        const emailValue = emailField.value;
        const passwordValue = passwordField.value;

        console.log("Tentative avec :", emailValue, passwordValue);

        if (emailValue === "supiii77@hotmail.com" && passwordValue === "260690") {
            messageDisplay.textContent = "Identifiant valide !";
            messageDisplay.style.color = "green";
        } else {
            messageDisplay.textContent = "Identifiant ou mot de passe incorrect.";
            messageDisplay.style.color = "red";
        }
    });
} else {
    alert("Erreur : Le bouton loginBtn n'a pas été trouvé dans le HTML !");
}