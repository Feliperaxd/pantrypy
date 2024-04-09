function copyText(text) {
    navigator.clipboard.writeText(text);
};

function clickCopyButton(clickedButton) {
  var buttons = document.getElementsByClassName('copy-button');
  for (var i = 0; i < buttons.length; i++) {
      buttons[i].style.animation = 'uncheckCopy 0.5s ease forwards';
  }
  clickedButton.style.animation = 'checkCopy 0.5s ease forwards';
};

function scrollToTop(thisButton, iframeId) {
  var iframe = document.getElementById(iframeId);
  thisButton.style.animation = 'slideUpScrollToTopButton 0.3s ease forwards';
  setTimeout(function() {
    iframe.contentWindow.scrollTo(
      {
        top: 0,
        behavior: 'smooth'
      }
    );
  }, 200);
};
