var menu = document.getElementById('menu');
var menuButton = document.getElementById('menu-button');
var backMenuButton = document.getElementById('back-menu-button');

menuButton.addEventListener('click', function(){
        menu.style.animation = 'openMenuAnimation 0.3s ease-in-out forwards';
    }
);
backMenuButton.addEventListener('click', function(){
        menu.style.animation = 'closeMenuAnimation 0.3s ease-in-out forwards';
    }
);