let currentFeedbackIndex = 0;
const feedbacks = document.querySelectorAll('.slider .feedback-field');
const prevBtnFeedback = document.querySelector('.slider .prevFeedback');
const nextBtnFeedback = document.querySelector('.slider .nextFeedback');

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