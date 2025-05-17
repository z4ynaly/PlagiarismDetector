const prompt = require('prompt-sync')();
const age = prompt('What is your age? ');



// if (age>10 && age<20){
//     console.log("True")
// }
// else{
//     console.log("false")
// }
// const n = prompt('Enter the number ');
// if (n%3==0 && n%2==0){
//     console.log("True")
// }
// else{
//     console.log("false")
// }

// switch(age){
//     case "12":
//         console.log("You are 12 yrs old!")
//         break
//     case "13":
//         console.log("You are 13 yrs old!")
//         break
//     case "14":
//         console.log("You are 14 yrs old!")
//         break
//     default:
//         console.log("You are not old enough!")
    
// }

if (age>=18){
    console.log("You can drive!")
}
else if (age<10){
    console.log("You cannot even think of driving!")
}
else{
    console.log("You cannot drive!")
}
