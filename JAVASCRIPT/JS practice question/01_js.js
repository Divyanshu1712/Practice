// // Arrow function

// const greet = () => console.log("Hello!");

// // greet()

const call = (a,b) =>{ 
   let sum = a + b;
   let sub = a-b;
   let sqaure = a**b;
   
   console.log(sum)
   console.log(sub)
   debugger;
   console.log(sqaure)
   console.error("error ")
}
call(10,5)

// arrow function in asynchoronus 

const person = {
    name: 'Divyanshu',
    greet: function() {
        setTimeout(() => {
            console.log(this.name);  // 'this' refers to 'person'
        }, 1000);
    }
};

person.greet();  // Output: "Divyanshu"
