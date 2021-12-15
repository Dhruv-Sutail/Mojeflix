console.log("dhruv");
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

function mobileMenu() {
    
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}
if(hamburger){
    hamburger.addEventListener("click", mobileMenu);
}


const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}