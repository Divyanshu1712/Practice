// Simple Calculator in JavaScript (Node.js version)

// Function to perform the calculation
function calculate(operation, num1, num2) {
    switch (operation) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            return num1 / num2;
        default:
            return "Invalid operation!";
    }
}

// Example usage:
// Replace 'operation' with '+', '-', '*', or '/' and replace 'num1' and 'num2' with numbers.

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter operation (+, -, *, /): ", function(operation) {
    rl.question("Enter the first number: ", function(num1) {
        rl.question("Enter the second number: ", function(num2) {
            num1 = parseFloat(num1);
            num2 = parseFloat(num2);

            let result = calculate(operation, num1, num2);
            console.log(`Result: ${num1} ${operation} ${num2} = ${result}`);
            rl.close();
        });
    });
});
