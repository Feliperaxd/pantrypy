const iframe = document.getElementById('main-iframe');
const mainHeader = document.getElementById('main-header');
const scrollToTopButton = document.getElementById('main-page-scroll-to-top-button');

iframe.contentWindow.addEventListener('scroll', function () {
    if (iframe.contentWindow.pageYOffset > 70) {
      mainHeader.style.animation = 'collapseHeader 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
      iframe.style.animation = 'expandIframe 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    }
    else {
      mainHeader.style.animation = 'expandHeader 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
      iframe.style.animation = 'collapseIframe 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    }

    if (iframe.contentWindow.pageYOffset > 100) {
      scrollToTopButton.style.animation = 'dropScrollToTopButton 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    }
    else {
      scrollToTopButton.style.animation = 'hideScrollToTopButton 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards';
    }
  }
);
