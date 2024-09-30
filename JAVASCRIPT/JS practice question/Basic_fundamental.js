"use strict";


//  printing things only 

console.log("Divyanshu")                // print single things without using semi colon
console.log("yeh lya hua ");            // using semi colon to print

// both print exact same

// variable declarations

const account_id = 15445                // can't change the system

let account_email = "divyanshu@google.com"   // this can change every were in code or in data 
var account_password = "12523"               // this can change every were in code or in data 

// account_city = "Basti"                       // we can declare the varibale like this too in js but this is not good pratice to do


//  now for this const and let only we to declare these varible to only not using var is not bad but in block code this seems some issue 

// account_id = 2222
account_email = " dibbu78@gmail.com"
// account_city = "noida"
console.log("New data after change " + account_password);
// console.log("New data after change " + account_city);
console.log("New data after change "+ account_email);
console.log(account_id)


// console.table([account_id,account_email,account_password,account_password]);        // print in table form to print new/ replace value

let name;     // this is undefind that means we delcare the varibale but didn't assign the value on it 
// console.log(name)  // output show undefind

// ******************** Data type  **********************
/*  
datatypes
1. number  number => 2 to power 53
2. string => ""
3. boolean => true/false
4. bigint
5. null => standalone value
6. undifend => 
7. Nan(not a number, type of this is number)
8. symbol => unique
*/


// ************************ TYPE CONVERSION  **********************
// TYPE conversion part 
// string conversion
let newNUm = 33
console.log(typeof newNUm);
let newNumisString = String(newNUm)
console.log(typeof newNumisString)
console.log(" here this only see in number form but he is string "+newNumisString);

// number conversion

let newName = "Divyanshu"
let newNameinNumber = Number(newName)
console.log(typeof newNameinNumber + " here is the form "+ newNameinNumber);


// object

console.log(typeof undefined); // undefined
console.log(typeof null); // object

//GAME COUNTER 

let gameCounter = 100
gameCounter++;
console.log(gameCounter);


// ********* formatted string  ********
let x = 15;
let y = 20;

let z = x + y;

console.log(`sum of ${x} and ${y} is ${z}`); // formattes string like in python we 'f{}'

//  meromry thing 

//  stack(Primitives)      heap(Non- Relitive)

let myName = "Divyanshu Srivastava";

let anotherName = myName;
anotherName = "dibbuLovlyNmae"
// console.log(anotherName);
// console.log(myName.slice(0,newNUm,1));

const fresh = "  Divyanshu-Sriavstava   "

console.log(fresh.trim())