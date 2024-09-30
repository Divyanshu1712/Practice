// Writing function 

// //  declartion are here
// console.log(greet("Divyashu")) // we ccan call function before intilization and it will work on and this  knows as HOSTED 

function greet(name){
    
    return `Hello ${name}, Good Morning!! You hava a nice day`
}


// function experession
// console.log(greetAgain("Anshika")) // HERE FUCNTION EXPERSION Is not hoiste so this will not work

const greetAgain = function(name){
    return `here this is fucntion experession,  NOW => hello ${name}, wlcome back you got good life man!!`

}

const add = (a,b) => a + b
const sub = (a,b) => a - b
const mult = (a,b) => a * b
const div = (a,b) => a / b
// console.log(add(2,4))
// console.log(div(2,4))
// console.log(sub(2,4))
// console.log(mult(2,4))

// const bigNUmber = BigInt(23723743179036900136903)

// console.log(bigNUmber)

console.log(typeof greet);
console.log(typeof greetAgain);
// console.

const arr = ["divyanshu","anshika", "love"]
console.log(typeof arr); // result shown Object becasue Non pritmive is always result as objects
console.log(arr[1]);

const myfuctio = name => `Hello, ${name}!`;
console.log(myfuctio = "Divanshu");
