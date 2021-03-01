const body = document.querySelector("body");

const IMG_NUM = 10;

function paintImage(imgNum) {
    const image = new Image();
    image.src = `images/${imgNum}.jpg`;
    image.classList.add("bgImg");
    body.prepend(image);
}

function genRandom() {
    const number = Math.ceil(Math.random() * IMG_NUM);
    return number;
}

function init() {
    const randomNum = genRandom();
    paintImage(randomNum)
}

init();