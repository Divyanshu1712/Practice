const cars = ['yolo','yamaan','toyota','lambo']
// cars.forEach(cars => console.log(cars));

//  iterrate for object 

const user = {name: 'John', age: 30};
for (let key in user) {
//   console.log(`${key}: ${user[key]}`);
}

// for esch 

const ages = [18, 2, 17];

const allAdult = ages.some(ages => ages >= 18);
console.log(allAdult)