const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;
const adminInterface = document.querySelector('.admin-interface');
const sections = document.querySelectorAll('.section');
const buttons = document.querySelectorAll('.section-buttons button');
const title = document.querySelector('.title');
    
darkModeToggle.addEventListener('change', () => {
    body.classList.toggle('dark-mode');
    adminInterface.classList.toggle('dark-mode');
    sections.forEach(section => section.classList.toggle('dark-mode'));
    buttons.forEach(button => button.classList.toggle('dark-mode'));
    title.classList.toggle('light-mode');
    title.classList.toggle('dark-mode');
});