


function getVideoBlock() {
    return document.querySelector(".video-block");
}
function getTestBlock() {
    return document.querySelector(".test-block");
}


function toggleDisplay(element) {
    if (element.style.display) {
        element.style.display = '';
    } else {
        element.style.display = 'none';
    }
}
function toggleTextAndVideoDisplay() {
    [getVideoBlock(), getTestBlock()].forEach(toggleDisplay)
}



let currentQuestion = 1;
const questions = new Map();
document.querySelectorAll('.question-body > *')
    .forEach((q, i) => questions.set(i + 1, q));




function moveToQuestion(number) {
    toggleDisplay(questions.get(currentQuestion));
    toggleDisplay(questions.get(number));
    currentQuestion = number;
}


function updateQLinkColor(qNumber) {
    let qLink = document.querySelector(`.question-link:nth-child(${qNumber})`);
    let isNotAnswered = true;
    for (let input of questions.get(qNumber).querySelectorAll('input')) {
        if (input.type === 'text' && input.value !== '') {
            isNotAnswered = false;
        } else if (input.checked) {
            isNotAnswered = false;
        }
    }
    if (isNotAnswered) {
        qLink.classList.remove('qlink-answered');
        qLink.classList.add('qlink-unanswered');
    } else {
        qLink.classList.add('qlink-answered');
        qLink.classList.remove('qlink-unanswered');
    }
}



document.querySelector(".nav-bar > .question-links").addEventListener("click", event => {
    if (event.target.classList.contains('question-link')) {
        moveToQuestion(parseInt(event.target.innerHTML));
    }
});

document.querySelector(".nav-bar > .nav-back").addEventListener("click", event => {
    console.log('back');
    if (currentQuestion === 1) {
        toggleTextAndVideoDisplay();
    } else {
        moveToQuestion(currentQuestion - 1);
    }
});
document.querySelector(".nav-bar > .nav-next").addEventListener("click", event => {
    console.log('next');
    if (currentQuestion === questions.size) {
        // send results
        console.log('sending results');
    } else {
        moveToQuestion(currentQuestion + 1);
    }
});


document.querySelector(".video-block button").addEventListener("click", toggleTextAndVideoDisplay);




