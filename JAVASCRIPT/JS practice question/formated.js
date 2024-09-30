// Write a function that takes three numbers as input and returns the largest number.

function mainNum(a,b,c){
    if (a > b &&  a > c){
        console.log(`${a} is greater`);
    }
    else if (b > a &&  b > c){
        console.log(`${b} is greater`);
    }else if (c > a &&  c > b){
        console.log(`${c} is greater`);
    }else{
        console.log("all three are equal!");
        
    }

}

mainNum(1,1,1)