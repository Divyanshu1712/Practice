const person = {
    name:'SD',
    age:'21',
    emmail:'sd12@google.com',
    getPersonInfo: function (){
        return `the name is ${this.name}, his age ${this.age}, and email ${this.emmail}`
    }
};



console.log(person.getPersonInfo());
// console.log(person.name);
// console.log(person['age']);

// person.age = 32
// console.log(person.age);

// person.sex = 'MALE'

// console.log(person);
