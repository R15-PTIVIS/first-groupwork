document.getElementById('downloadBtn').addEventListener('click', () => {
  const canvas = document.getElementById('drawingCanvas');
  const imageData = canvas.toDataURL('image/png');

  const link = document.createElement('a');
  link.href = imageData;
  link.download = 'drawing.png';
  link.click();
});