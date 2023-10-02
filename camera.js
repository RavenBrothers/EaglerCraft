 const camera = document.querySelector('.camera');
        let cameraX = 0;
        const speed = 25; // Adjust the speed of the camera movement here
        const maxTranslation = 2500; // Adjust the maximum translation distance here

        const animateCamera = () => {
            if (cameraX < maxTranslation) {
                cameraX += speed; // Use the 'speed' variable
                camera.style.transform = `translateX(${cameraX}px)`;
                requestAnimationFrame(animateCamera);
            } else {
                // Reset the animation when it reaches the maximum distance
                cameraX = 0;
                camera.style.transform = `translateX(${cameraX}px)`;
                requestAnimationFrame(animateCamera);
            }
        }

        animateCamera();
