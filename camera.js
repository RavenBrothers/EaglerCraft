const camera = document.querySelector('.camera');
let cameraX = 0;

function animateCamera() {
   cameraX += 1; // Adjust the speed of the camera movement here
   camera.style.transform = `translateX(${cameraX}px)`;
   requestAnimationFrame(animateCamera);
}

animateCamera();
