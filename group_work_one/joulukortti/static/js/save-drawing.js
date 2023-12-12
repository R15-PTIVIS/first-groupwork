document.getElementById('saveDrawing').addEventListener('click', function(event) {
    event.preventDefault();

    // Get the canvas and convert its content to a data URL (base64 encoded image)
    var canvas = document.getElementById('drawingCanvas');
    var imageData = canvas.toDataURL('image/png');

    // Get the drawing name
    var drawingName = document.getElementById('drawingName').value;

var url = document.getElementById('saveDrawing').getAttribute('data-url');
console.log('URL:', url);
console.log('CSRF Token:', getCookie('csrftoken'));
var dataToSend = JSON.stringify({ name: drawingName, image: imageData });
console.log('Data being sent:', dataToSend);

    // Send the data to the Django backend using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // Add CSRF token

    xhr.onload = function () {
        if (this.status == 200) {
            console.log("Drawing saved successfully.");
            // Handle success, maybe redirect or show a message
            window.location.href = '/gallery/';
        } else {
            console.error("Error saving drawing.");
            // Handle error
        }
    };

    xhr.send(JSON.stringify({ name: drawingName, image: imageData }));
});

// Function to get CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim(); // Use native JavaScript trim method
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
