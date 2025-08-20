
document.addEventListener('DOMContentLoaded', function () {
  const dropdowns = document.querySelectorAll('.nav-item.dropdown');
  const themeSwitch = document.getElementById('themeSwitch');
  const themeIcon = document.getElementById('themeIcon');

  // Hover para mega menú desktop
  dropdowns.forEach(dropdown => {
    dropdown.addEventListener('mouseenter', () => {
      if (window.innerWidth > 991) {
        dropdown.classList.add('show');
        dropdown.querySelector('.dropdown-menu').classList.add('show');
      }
    });
    dropdown.addEventListener('mouseleave', () => {
      if (window.innerWidth > 991) {
        dropdown.classList.remove('show');
        dropdown.querySelector('.dropdown-menu').classList.remove('show');
      }
    });
  });

  // Modo oscuro: cargar preferencia y toggle
  const darkMode = localStorage.getItem('darkMode');
  if (darkMode === 'enabled') {
    document.body.classList.add('dark-mode');
    themeSwitch.checked = true;
    themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
  }

  themeSwitch.addEventListener('change', () => {
    if (themeSwitch.checked) {
      document.body.classList.add('dark-mode');
      localStorage.setItem('darkMode', 'enabled');
      themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    } else {
      document.body.classList.remove('dark-mode');
      localStorage.setItem('darkMode', 'disabled');
      themeIcon.classList.replace('bi-sun-fill', 'bi-moon-fill');
    }
  });

  // Navbar efecto al hacer scroll (opcional)
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
});

document.querySelectorAll('.nav-item.dropdown').forEach(item => {
  item.addEventListener('mouseenter', () => {
    const menu = item.querySelector('.dropdown-menu');
    item.classList.add('show');
    menu.classList.add('show');
  });
  item.addEventListener('mouseleave', () => {
    const menu = item.querySelector('.dropdown-menu');
    item.classList.remove('show');
    menu.classList.remove('show');
  });
});
