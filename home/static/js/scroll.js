
document.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar-custom");
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

// Agrega esto antes de cerrar el </body>
document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");

    // Estado inicial
    navbar.classList.add("navbar-transparent");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.classList.remove("navbar-transparent");
            navbar.classList.add("navbar-scrolled");
        } else {
            navbar.classList.add("navbar-transparent");
            navbar.classList.remove("navbar-scrolled");
        }
    });
});

