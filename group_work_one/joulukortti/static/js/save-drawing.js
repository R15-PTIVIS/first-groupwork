// save-drawing.js

document.getElementById('saveBtn').addEventListener('click', () => {
    // Get the drawing name from the input field
    const drawingName = document.getElementById('drawingName').value;

    // Get the canvas element and its context
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');

    // Convert the canvas content to a data URL representing a PNG image
    const imageData = canvas.toDataURL('image/png');

    // Send the drawing name and image data to the server for saving
    saveDrawing(drawingName, imageData);
});

function saveDrawing(name, imageData) {
    // Use AJAX or fetch to send the drawing data to the server
    // In the server, you'll need to handle saving the image data to the database
    // You can use Django's ORM to create a new XmasCard object with the provided data
    // For simplicity, this example assumes the existence of a Django view named save_drawing

    fetch('/save_drawing/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token for security
        },
        body: JSON.stringify({
            name: name,
            image_data: imageData,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Drawing saved successfully:', data);
        // You can add additional handling here if needed
    })
    .catch(error => {
        console.error('Error saving drawing:', error);
    });
}

// Function to get CSRF token from cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
