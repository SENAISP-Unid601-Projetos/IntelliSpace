const luz = document.getElementById('luz');

luz.addEventListener('mouseenter', () => {
  luz.classList.add('acesa');
});

luz.addEventListener('mouseleave', () => {
  luz.classList.remove('acesa');
});

