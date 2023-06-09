let currentImageIndex = 0;
const images = document.querySelectorAll('.advertisementImg');
const prevBtn = document.querySelector('.slider .prev');
const nextBtn = document.querySelector('.slider .next');

function showImage(index) {
    console.log(images.length);
    images.forEach(imag => imag.classList.remove('active'))
    images[index].classList.add('active');
    currentImageIndex = index;
}

prevBtn.addEventListener('click', () => {
    console.log(images.length)
    if (currentImageIndex === 0) {
        showImage(images.length - 1);
    } else {
        showImage(currentImageIndex - 1);
    }
});

nextBtn.addEventListener('click', () => {
        console.log(images.length)
    if (currentImageIndex === images.length - 1) {
        showImage(0);
    } else {
        showImage(currentImageIndex + 1);
    }
});


showImage(0);


