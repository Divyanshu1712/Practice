const newArr = [1,2,3,4,5]
console.log(` This is main array  ${newArr}`);

// push
newArr.push(3);
// console.log(`the push function used at this time means add item in last   ${newArr}     see 3 is added at last`);

// pop
newArr.pop(5);
// console.log(`the pop function used at this time means remove last item    ${newArr}     see 3 is reomve from last `);

// unshift
newArr.unshift(5);
// console.log(`the unshift function used at this time means add first  item  ${newArr}    see 5 is added at first  `);

// shift 
newArr.shift(5);
// console.log(`the shift function used at this time means add remove  item  ${newArr}    see 5 is remove at first  `);

// slice 
const new1 = newArr.slice(1,3);
console.log(`In this slice fucntion only return the removed array of item ${new1}   `);
console.log(newArr);


// splice


const new2 = newArr.splice(2,5)
console.log(` here i use splice fucntion for array  ${new2}`);

console.log(newArr);
