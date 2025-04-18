const menuIcon = document.querySelector('.menu-icon');// Menú hamburguesa
const navLinks = document.querySelector('.nav-links');// Header oculto en scroll
const header = document.querySelector('.header');// Header oculto en scroll

// G E N E R A L

//MENU HAMBURGUESA
console.log(menuIcon); // ¿Es null o tiene un elemento?
console.log(navLinks); // ¿Es null o tiene un elemento?
menuIcon.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

//HEADER OCULTO EN SCROLL
let prevScrollPos = window.scrollY;
let isScrolling;
window.onscroll = function () {
    window.clearTimeout(isScrolling);
    isScrolling = setTimeout(() => {
        let currentScrollPos = window.scrollY;
        if (prevScrollPos > currentScrollPos) {
            header.style.top = "0";
        } else {
            header.style.top = "-80px";
        }
        prevScrollPos = currentScrollPos;
    }, 100);
};

// L O C A T I O N . H T M L

//VER HORARIO AL HACER CLICK
document.querySelectorAll('.schedule-card').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('active');
    });
  });  


