// Set initial background color to white
const initialBackgroundColor = '#ffffff';

// Function to set the background color without clearing the drawing
function setBackgroundColor(color) {
  ctx.fillStyle = color;
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// Ensure the DOM is fully loaded before attaching the click event listeners
document.addEventListener('DOMContentLoaded', () => {
  // Declare canvas and ctx inside the DOMContentLoaded event
  const canvas = document.getElementById('drawingCanvas');
  const ctx = canvas.getContext('2d');

  // Set initial background color
  setBackgroundColor(initialBackgroundColor);

  // Attach click event listeners
  document.querySelectorAll('.background-color').forEach((swatch) => {
    swatch.addEventListener('click', () => {
      const color = swatch.dataset.color;
      setBackgroundColor(color);
    });
  });

  document.querySelectorAll('.line-color').forEach((swatch) => {
    swatch.addEventListener('click', () => {
      const color = swatch.dataset.color;
      canvas.getContext('2d').strokeStyle = color;
    });
  });
});