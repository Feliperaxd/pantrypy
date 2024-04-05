const iframe = document.getElementById('main-iframe');
const mainHeader = document.getElementById('main-header');

iframe.contentWindow.addEventListener('scroll', function () {
    if (iframe.contentWindow.pageYOffset > 70) {
      mainHeader.style.animation = 'collapseHeader 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
      iframe.style.animation = 'expandIframe 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    } 
    else {
      mainHeader.style.animation = 'expandHeader 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
      iframe.style.animation = 'collapseIframe 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    }
  }
);