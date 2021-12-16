function playTheGame(){
    let response = confirm(`Do You Like Scary Movies?, just kidding,  Would you like to play a game?`)
    let userNumber;
    let computerNumber = parseInt((Math.random()*10)+1)
    console.log(computerNumber)
    if (response == false) {
        console.log("No Problem, Goodbye")
        return "No Problem, Goodbye";
    } else {
        userNumber = Number(prompt("Enter a number between 0-10"))
    }
    if (isNaN(userNumber)) {
        alert("Sorry, not a number. Goodbye")
    } else if (userNumber > 10 || userNumber < 1){
        alert("Sorry, not a good number")
    } else {
        test(userNumber, computerNumber)
    } 

    
}



function test(userNumber, computerNumber){
    let numberOfChances = 10
    while (numberOfChances < 3)
        if (userNumber == computerNumber){
            alert("Winner")
        } else if(numberOfChances.length == numOfChances){
            alert("Game Over");
            break
        } else if (userNumber > computerNumber){
            alert("Your number is Larger then the computer's, guess again");
            userNumber = prompt("please try again:")
            numberOfChances.push(userNumber);
        } else if (computerNumber > userNumber); {
            alert("Your Number is Smaller then the computer's, please try again");
            userNumber = prompt("please try again: ")
            numberOfChances.push(userNumber)
        }


    }

