        const openConsoleButton = document.getElementById("openConsoleButton");
        const closeConsoleButton = document.getElementById("closeConsoleButton");
        const consoleModal = document.getElementById("consoleModal");
        const consoleDiv = document.getElementById("console");
        const input = document.getElementById("input");

        // Function to display a message in the console
        function writeToConsole(message) {
            consoleDiv.innerHTML += message + "<br>";
            consoleDiv.scrollTop = consoleDiv.scrollHeight;
        }

        // Function to handle user input
        function handleInput() {
            const command = input.value.trim();
            input.value = "";

            // Display the entered command in the console
            writeToConsole(input.placeholder + command);

            writeToConsole("Command not recognized: " + command);
        }

        // Handle Enter key press in the input field
        input.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                handleInput();
            }
        });

        // Open the console when the button is clicked
        openConsoleButton.addEventListener("click", function() {
            consoleModal.style.display = "block";
        });

        // Close the console when the close button is clicked
        closeConsoleButton.addEventListener("click", function() {
            consoleModal.style.display = "none";
        });

        writeToConsole("Eaglercraft by EaglerDevs [Version 0.0.1-alpha]");
        writeToConsole("(c) Eagler Devs. All rights reserved.");
        writeToConsole("");
        writeToConsole("EAGLER:\\> Welcome to the Web Dev Console");
        writeToConsole("EAGLER:\\> Type 'help' for a list of commands.");
