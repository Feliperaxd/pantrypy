var menu = document.getElementById('menu-nav');
var menuButton = document.getElementById('menu-button');
var backMenuButton = document.getElementById('back-menu-button');

menuButton.addEventListener('click', function(){
        menu.style.animation = 'openMenu 0.3s ease-in-out forwards';
    }
);
backMenuButton.addEventListener('click', function(){
    menu.style.animation = 'closeMenu 0.3s ease-in-out forwards';
}
);