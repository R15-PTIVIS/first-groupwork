// color-picker.js

document.querySelectorAll('.background-color').forEach((swatch) => {
  swatch.addEventListener('click', () => {
    const color = swatch.dataset.color;
    const canvas = document.getElementById('drawingCanvas');
    const ctx = canvas.getContext('2d');

    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw a filled rectangle with the chosen background color
    ctx.fillStyle = color;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  });
});


document.querySelectorAll('.line-color').forEach((swatch) => {
  swatch.addEventListener('click', () => {
    const color = swatch.dataset.color;
    document.getElementById('drawingCanvas').getContext('2d').strokeStyle = color;
  });
});
