//Write a program to check whether a number is positive, negative, or zero using if, else if, else

function check(num){
    if (num  == 0){
        console.log(`Number is zero`);
    }
    else if (num < 0){
        console.log("number is negative")
    }
    else{
        console.log("Number is Postive")
    }
}

check(12)
check(0.01313)
check(-122)
check(0)