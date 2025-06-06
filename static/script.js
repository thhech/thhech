async function sendMessage() {
    const input = document.getElementById('input');
    const text = input.value;
    if (!text) return;

    appendMessage('Du', text);
    input.value = '';

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
    });
    const data = await response.json();
    appendMessage('Bot', data.reply);
}

function appendMessage(sender, text) {
    const messages = document.getElementById('messages');
    const div = document.createElement('div');
    div.textContent = `${sender}: ${text}`;
    messages.appendChild(div);
}
