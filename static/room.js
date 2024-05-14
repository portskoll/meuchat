const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);
const chatSocket = new WebSocket(
    "wss://" +
    window.location.host +
    "/ws/" +
    roomName +
    "/"
);

chatSocket.onmessage = function (e) {
    console.log('onmessege')
    const data = JSON.parse(e.data);

    if (data.message) {
        let html = '<div class="p-4 m-2 bg-gray-200 rounded-xl">';
        html += '<p class="font-semibold">' + data.username + '</p>';
        html += '<p>' + data.message + '</p></div>';

        document.querySelector('#chat-messages').innerHTML += html;
        scrollToBottom();

    } else {
        alert('A mensagem está vazia!')
    }
}

chatSocket.onclose = function (e) {
    console.log('onclose')
}

document.querySelector('#chat-message-submit').onclick = function (e) {
    e.preventDefault();

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';
    return false;
}

function scrollToBottom() {
    const objDiv = document.querySelector('#chat-messages');
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();

