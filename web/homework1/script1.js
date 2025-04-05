let display = document.getElementById('display');
let currentInput = '';
let lastInput = '';

// 添加数字到当前输入
function appendNumber(number) {
    // 禁止输入多个连续的0
    if (number === 0 && currentInput === '0') return;
    // 如果当前输入是0，清空输入
    if (currentInput === '0') currentInput = '';
    currentInput += number;
    updateDisplay();
}

// 添加运算符到当前输入
function appendOperator(operator) {
    // 如果当前输入为空且不是负号，不允许输入运算符
    if (currentInput === '' && operator !== '-') return;
    // 如果上一个输入是运算符，不允许重复输入
    if (isOperator(lastInput)) return;
    currentInput += operator;
    updateDisplay();
}

// 添加小数点
function appendDot() {
    // 如果当前输入已经包含小数点，不允许重复输入
    if (currentInput.includes('.')) return;
    currentInput += '.';
    updateDisplay();
}

// 清空显示屏
function clearDisplay() {
    currentInput = '';
    updateDisplay();
}

// 计算结果
function calculateResult() {
    try {
        currentInput = eval(currentInput).toString();
        updateDisplay();
    } catch (e) {
        // 输入无效时提示用户
        alert('输入无效');
        clearDisplay();
    }
}

// 更新显示屏
function updateDisplay() {
    display.value = currentInput;
    lastInput = currentInput.slice(-1);
}

// 判断字符是否为运算符
function isOperator(char) {
    return ['+', '-', '*', '/'].includes(char);
}