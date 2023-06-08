const images = document.querySelectorAll('.slider img');
const feedbacks = document.querySelectorAll('.slider .feedback-field');
const prevBtn = document.querySelector('.slider .prev');
const nextBtn = document.querySelector('.slider .next');
let currentImageIndex = 0;
let currentFeedbackIndex = 0;
const prevBtnFeedback = document.querySelector('.slider .prevFeedback');
const nextBtnFeedback = document.querySelector('.slider .nextFeedback');

function showImage(index) {
    images.forEach(image => image.classList.remove('active'));
    images[index].classList.add('active');
    currentImageIndex = index;
}

prevBtn.addEventListener('click', () => {
    if (currentImageIndex === 0) {
        showImage(images.length - 1);
    } else {
        showImage(currentImageIndex - 1);
    }
});

nextBtn.addEventListener('click', () => {
    if (currentImageIndex === images.length - 1) {
        showImage(0);
    } else {
        showImage(currentImageIndex + 1);
    }
});

showImage(0);

function showFeedback(index) {
    feedbacks.forEach( feedback => feedback.classList.remove('active'));
    feedbacks[index].classList.add('active');
    currentFeedbackIndex = index;
}

prevBtnFeedback.addEventListener('click', () => {
    if (currentFeedbackIndex === 0) {
        showFeedback(feedbacks.length - 1);
    } else {
        showFeedback(currentFeedbackIndex - 1);
    }
});

nextBtnFeedback.addEventListener('click', () => {
    if (currentFeedbackIndex === feedbacks.length - 1) {
        showFeedback(0);
    } else {
        showFeedback(currentFeedbackIndex + 1);
    }
});

showFeedback(0);