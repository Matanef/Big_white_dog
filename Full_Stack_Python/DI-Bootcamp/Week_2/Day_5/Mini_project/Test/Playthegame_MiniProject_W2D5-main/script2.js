function playTheGame(){
    let userAnswer = confirm("Would you like to play a game?");
    let userNumber;

    if (userAnswer == false) {
        alert("No problem, Goodbye.");
    } else{
        userNumber = parseInt(prompt("Enter a number between 0-10"))
    }
    if (isNaN(userNumber)){
        alert("this is not a number")
    } else if (userNumber<0 || userNumber>10) {
        alert(`Numbers needs to be between 0 and 10, the number you selected is ${userNumber}`)
    }
    console.log(userNumber);
    console.log(typeof(userNumber));
    let computerNumber = Math.floor(Math.random() * 10) + 1;
    console.log(computerNumber);
    return userNumber
    return computerNumber
}

// let x = userNumber;
// let y = computerNumber;
// console.log(x);
// console.log(y);




function test(userNumber,computerNumber){
    let x = userNumber
    let y = computerNumber;
    let newNumber;
    if (x > y) {
        let newNumber = prompt("Your number is bigger then the computer’s, guess again")
    } else if (x < y){
        let newNumber = prompt("Your number is smaller then the computer’s, guess again")
    }else if (x==y){
        alert("Winner");

    }
}

// test();
