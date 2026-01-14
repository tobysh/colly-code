let currentLayer = null;
let layers = [];
let drawing = false;
let tool = "brush"; // or "eraser"

const canvasArea = document.getElementById("canvasArea");

// Create initial layer
addLayer();

function addLayer() {
    const canvas = document.createElement("canvas");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight - 60;
    canvas.style.zIndex = layers.length;

    const ctx = canvas.getContext("2d");
    ctx.lineCap = "round";

    canvasArea.appendChild(canvas);
    layers.push({ canvas, ctx });
    currentLayer = layers[layers.length - 1];

    console.log("Layer added:", layers.length);
}

document.getElementById("addLayerBtn").onclick = addLayer;

document.getElementById("brushBtn").onclick = () => tool = "brush";
document.getElementById("eraserBtn").onclick = () => tool = "eraser";

document.addEventListener("mousedown", e => startDraw(e));
document.addEventListener("mousemove", e => draw(e));
document.addEventListener("mouseup", () => drawing = false);

function startDraw(e) {
    drawing = true;
    draw(e);
}

function draw(e) {
    if (!drawing) return;

    const rect = canvasArea.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ctx = currentLayer.ctx;

    const size = document.getElementById("brushSize").value;
    ctx.lineWidth = size;

    if (tool === "brush") {
        ctx.strokeStyle = document.getElementById("colorPicker").value;
    } else if (tool === "eraser") {
        ctx.strokeStyle = "#666"; // background color
    }

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
}

document.getElementById("downloadBtn").onclick = () => {
    // Merge layers into a single temp canvas
    const finalCanvas = document.createElement("canvas");
    finalCanvas.width = layers[0].canvas.width;
    finalCanvas.height = layers[0].canvas.height;
    const finalCtx = finalCanvas.getContext("2d");

    layers.forEach(l => {
        finalCtx.drawImage(l.canvas, 0, 0);
    });

    const link = document.createElement("a");
    link.href = finalCanvas.toDataURL("image/png");
    link.download = "artwork.png";
    link.click();
};
