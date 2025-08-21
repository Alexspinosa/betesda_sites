# Comandos Git - Proyecto Betesda Sites

## Inicialización y configuración

**git init**
Crea un repositorio Git en tu proyecto local.
Después de esto, tu carpeta empieza a ser “versionada” por Git.

**git remote add origin URL**
Conecta tu repositorio local con un repositorio remoto (GitHub).
`URL` es la dirección de tu repositorio en GitHub.

---

## Agregar y guardar cambios

**git add .**
Agrega todos los cambios (archivos nuevos o modificados) al “staging area”, preparándolos para el commit.

**git commit -m "mensaje"**
Guarda los cambios en el historial de Git con un mensaje que describe qué hiciste.

---

## Ramas

**git branch**
Lista las ramas locales en tu repositorio.
La rama con `*` es en la que estás actualmente.

**git branch <nombre_rama>**
Crea una nueva rama llamada `<nombre_rama>`.

**git checkout <nombre_rama>**
Cambia a la rama `<nombre_rama>` para trabajar en ella.

**git branch -M main**futuros `git push` y `git pull` sean automáticos.

---

## Comprobación de estado

**git status**
Muestra en qué rama estás, si hay archivos modificados, sin agregar, sin commitear, etc.

**git log**
Muestra el historial de commits de la rama actual (no lo usamos todavía, pero es útil).
