// canvas-drawing.js

const canvas = document.getElementById('drawingCanvas');
const ctx = canvas.getContext('2d');

// Set up initial drawing properties
size = 1;
ctx.lineCap = 'round';
ctx.strokeStyle = '#000';

let isDrawing = false;

//stores draw events as a stack
let drawStack = [];
//stores individual draw event as a stack
let drawInstance = [];

var mousePosition = {x:0,y:0}

document.querySelectorAll('.lineWidthBtn').forEach((button) => {
    button.addEventListener('click', () => {
        size = button.dataset.size;
        canvas.getContext('2d').lineWidth = size;
    });
});

document.querySelector('#undoButton').addEventListener('click', () => {
    drawStack.splice(-1, 1);
    draw();
});

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    previous = { x: mousePosition.x, y: mousePosition.y };
    mousePosition = { x: e.clientX - canvas.offsetLeft, y: e.clientY - canvas.offsetTop }
    //resets previous draw event
    drawInstance = [];
    //initiates this draw instance into the drawInstance stack
    drawInstance.push({ x: mousePosition.x, y: mousePosition.y, size: size});
});

canvas.addEventListener('mousemove', (e) => {
    if (isDrawing)
    {
        previous = { x: mousePosition.x, y: mousePosition.y };
        mousePosition = { x: e.clientX - canvas.offsetLeft, y: e.clientY - canvas.offsetTop }
        drawInstance.push({ x: mousePosition.x, y: mousePosition.y });
        //continually draws on canvas
        ctx.beginPath();
        ctx.moveTo(previous.x, previous.y);
        ctx.lineTo(mousePosition.x, mousePosition.y);
        ctx.stroke();
    }
});

canvas.addEventListener('mouseup', () => {
    isDrawing = false;
    //pushes this drawInstance stack into the overall drawStack
    drawStack.push(drawInstance);
});

function draw()
{
    ctx.fillStyle = draw.BGcolor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    drawStack.forEach(draw =>
    {
        //begins drawing from the first coordinates on the drawStack
        ctx.beginPath();
        ctx.moveTo(draw[0].x, draw[0].y);
        ctx.lineWidth = draw[0].size;
        //iterates through the drawStack
        for (let i = 1; i < draw.length; i++)
        {
            ctx.lineWidth = draw[i].size;
            ctx.lineTo(draw[i].x, draw[i].y);
        }
        
        ctx.stroke();
    })
}

