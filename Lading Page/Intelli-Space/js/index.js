let slider = document.querySelector('.slider');
let sliderItems = document.querySelectorAll('.slider img');
let currentIndex = 0;
const slideWidth = sliderItems[0].clientWidth;

function nextSlide() {
    currentIndex++;
    if (currentIndex >= sliderItems.length) {
        currentIndex = 0;
    }
    updateSlider();
}

function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

setInterval(nextSlide, 2000); // Altera o slide a cada 1 segundos
