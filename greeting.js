const greetingForm = document.querySelector(".js-greetingForm"),
    greetingInput = greetingForm.querySelector("input"),
    greetingText = document.querySelector(".js-greetingText");

const USER_LS = "currentUser"
    SHOWING_CN = "showing"

function saveName(text) {
    localStorage.setItem(USER_LS, text);
}

function handleSubmitGreet(event) {
    event.preventDefault();
    const currentValue = greetingInput.value;
    paintGreet(currentValue);
    saveName(currentValue);
}

function askForName() {
    greetingForm.classList.add(SHOWING_CN);
    greetingForm.addEventListener("submit", handleSubmitGreet)
}

function paintGreet(text) {
    greetingForm.classList.remove(SHOWING_CN);
    greetingText.classList.add(SHOWING_CN);
    greetingText.innerText = `Hello, ${text}`
}

function loadName() {
    const currentUser = localStorage.getItem(USER_LS)
    if (currentUser === null) {
        askForName();
    } else {
        paintGreet(currentUser);
    }
}

function init() {
    loadName();
}

init();