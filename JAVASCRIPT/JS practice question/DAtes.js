// Dates

// let myDate = new Date();
// console.log(myDate.toDateString()); 
// console.log(myDate.toString());
// console.log(myDate.getTimezoneOffset());
// console.log(myDate.getFullYear());
// console.log(myDate.toISOString());
// console.log(myDate.toLocaleString());

// const createDate = new Date(2023,5,23);
// console.log(createDate.toDateString());
 
const code1 = () =>{
    const myMonth = new Date()
    console.log(myMonth);
    // console.log(typeof myMonth)
    return myMonth   
}



const code2 = () => {
    const myMonth1 =  Date()
    // console.log(typeof myMonth1)
    console.log(myMonth1);
    // console.log(`we got this when we create String as  == ${myMonth1}`);
    return myMonth1
}

if (code1() === code2()){
    console.log(true)
}
else{
    console.log(false)

}