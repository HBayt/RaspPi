document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêche la soumission du formulaire

    // Exemple d'URL d'image à afficher
    const imageUrl = 'https://via.placeholder.com/600'; // Remplacez par l'URL de votre image

    const displayedImage = document.getElementById('displayedImage');
    displayedImage.src = imageUrl;
    displayedImage.style.display = 'block';
});