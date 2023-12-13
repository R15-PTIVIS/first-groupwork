// canvas-drawing.js

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');

// Set up initial drawing properties
size = 3;
ctx.lineCap = 'round';
ctx.strokeStyle = '#000';

let isDrawing = false;

document.querySelectorAll('.lineWidthBtn').forEach((button) => {
    button.addEventListener('click', () => {
        size = button.dataset.size;
        canvas.getContext('2d').lineWidth = size;
    });
});

canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  draw(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
});

canvas.addEventListener('mousemove', (e) => {
  if (isDrawing) {
    draw(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
  }
});

canvas.addEventListener('mouseup', () => {
  isDrawing = false;
  ctx.beginPath();
});

function draw(x, y) {
    ctx.lineWidth = size;
  ctx.lineTo(x, y);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x, y);
}

