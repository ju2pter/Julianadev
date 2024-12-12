const output = document.getElementById('output');
const input = document.getElementById('terminal-input');

const commands = {
    help: "Available commands: <span style='color: #00ff00;'>help</span>, <span style='color: #00ff00;'>about</span>, <span style='color: #00ff00;'>clear</span>",
    about: "Juliana's Cyber Lab is a place for exploring cybersecurity and backend development.",
    clear: ""
};

input.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        const command = input.value.trim();
        executeCommand(command);
        input.value = '';
    }
});

function executeCommand(command) {
    if (commands[command]) {
        output.innerHTML += `<div>${command}: ${commands[command]}</div>`;
        if (command === "clear") {
            output.innerHTML = "";
        }
    } else {
        output.innerHTML += `<div>${command}: Command not found</div>`;
    }
    output.scrollTop = output.scrollHeight;
}
