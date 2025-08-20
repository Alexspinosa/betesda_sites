// Texto principal y cita
const verso = '"Jesucristo es el mismo ayer, y hoy, y por los siglos."';
const cita = '— Hebreos 13:8';

// Paletas de colores
const coloresVerso = ["#ffffff", "#ffd700", "#ff4500", "#00ced1"];
const coloresCita = ["#ffd700", "#ff69b4", "#adff2f", "#1e90ff"];

// Elementos HTML
const mainEl = document.getElementById("typewriter-main");
const citaEl = document.getElementById("typewriter-cita");

let i = 0;
let j = 0;

// Efecto máquina de escribir para el verso
function escribirFrase() {
  if (i < verso.length) {
    let span = document.createElement("span");
    span.textContent = verso.charAt(i);
    span.style.color = coloresVerso[i % coloresVerso.length]; // color cíclico
    mainEl.appendChild(span);

    i++;
    setTimeout(escribirFrase, 50); // velocidad
  } else {
    setTimeout(escribirCita, 500); // espera antes de la cita
  }
}

// Efecto máquina de escribir para la cita
function escribirCita() {
  if (j < cita.length) {
    let span = document.createElement("span");
    span.textContent = cita.charAt(j);
    span.style.color = coloresCita[j % coloresCita.length];
    citaEl.appendChild(span);

    j++;
    setTimeout(escribirCita, 40);
  }
}

// Inicia la animación cuando el DOM está listo
document.addEventListener("DOMContentLoaded", escribirFrase);
