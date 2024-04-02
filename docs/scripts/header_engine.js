window.addEventListener('scroll', function(){
    var headerElement = document.querySelector('header');
    if (window.scrollY > 0) {
      headerElement.style.height = '1000px'
    } 
    else {
      headerElement.style.height = '100px'
    }
  }
);