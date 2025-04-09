const carouselImages = document.getElementById('carouselImages');
const prevButton = document.getElementById('prevButton');
const nextButton = document.getElementById('nextButton');
const carouselDots = document.getElementById('carouselDots');

const images = document.querySelectorAll('.carousel-images img');
const totalImages = images.length;

let currentIndex = 0;
let timer;

// 初始化圆点导航
function initDots() {
    const dots = document.querySelectorAll('.dot');
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            goToSlide(index);
            resetTimer();
        });
    });
}

// 更新圆点状态
function updateDots() {
    const dots = document.querySelectorAll('.dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
    });
}

// 切换到指定幻灯片
function goToSlide(index) {
    currentIndex = (index + totalImages) % totalImages;
    carouselImages.style.transform = `translateX(-${currentIndex * 600}px)`; // 确保每次移动一个图片的宽度
    updateDots();
}

// 上一张图片
function prevSlide() {
    goToSlide(currentIndex - 1);
    resetTimer();
}

// 下一张图片
function nextSlide() {
    goToSlide(currentIndex + 1);
    resetTimer();
}

// 自动轮播
function startAutoPlay() {
    timer = setInterval(() => {
        nextSlide();
    }, 2000);
}

// 重置定时器
function resetTimer() {
    clearInterval(timer);
    startAutoPlay();
}

// 初始化
prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);
initDots();
startAutoPlay();