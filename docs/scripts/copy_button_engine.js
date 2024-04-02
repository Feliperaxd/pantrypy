function copyText(text) {
    navigator.clipboard.writeText(text)
}

function changeColor(clickedButton) {
    var buttons = document.getElementsByClassName('copy-text-button');

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].style.backgroundColor = '';
    }

    clickedButton.style.backgroundColor = 'red';
}