function copyText(text) {
    navigator.clipboard.writeText(text)
}

function clickCopyButton(clickedButton) {
    var buttons = document.getElementsByClassName('copy-button');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].style.animation = 'uncheckCopy 0.5s ease forwards';
        buttons[i].style.animation = 'none';
    }
    clickedButton.style.animation = 'checkCopy 0.5s ease forwards';
}