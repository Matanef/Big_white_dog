// let signsArr = [
// {sign: "+"},
// {sign: "-"},
// {sign: "/"},
// {sign: "*"}
// ]

// let numArr = [
// ]

let paraElement = document.getElementsByClassName("container");
let newElement = document.createElement('div');




function getRandomInt (a_min, a_max){
	a_min = Math.ceil(a_min);
	a_max = Math.floor(a_max);
	return Math.floor(Math.random() * (a_max - a_min + 1)) + a_min;
}
let firstNumbers = getRandomInt()
let genNum = firstNumbers
console.log(genNum);

function enclose (a_number){
	if (a_number < 0){
		return "(" + a_number + ")";
	}

	return a_number.toString();
}

function generateRandomEquation (){
	let l_numbers = getRandomInt(2, 3);
	let l_operations = l_numbers - 1;


	let l_numberArray = [];
	let l_opArray = [];


	for (let i = 0; i < l_numbers; ++i)	{
		let l_number = getRandomInt(1, 20);
		let l_invert = getRandomInt(0, 1);
		if (l_invert === 0)
			l_numberArray.push(-l_number);
		else
			l_numberArray.push(l_number);
	}


	for (let i = 0; i < l_operations; ++i){
        // 0: Addition
        // 1: Subtraction
        // 2: Multiplication
        // 3: Division
        l_opArray.push(getRandomInt(0, 3));
    }


    let l_result = l_numberArray[0];
    let l_string = l_numberArray[0];
    for (let i = 1; i < l_numbers; ++i){

    	switch (l_opArray[i - 1]){
    		case 0:
    		l_result += l_numberArray[i];
    		l_string += " + " + enclose(l_numberArray[i]);
    		break;
    		case 1:
    		l_result -= l_numberArray[i];
    		l_string += " - " + enclose(l_numberArray[i]);
    		break;
    		case 2:
    		l_result *= l_numberArray[i];
    		l_string += " * " + enclose(l_numberArray[i]);
    		break;
    		case 3:
    		l_result /= l_numberArray[i];
    		l_string += " / " + enclose(l_numberArray[i]);
    		break;

    	}
    }


    l_string += " = " + l_result;
    return l_string;

}

let values = generateRandomEquation();
let resultOut = values.result;
console.log(resultOut)

$("#btn-generate").click(function () {
	$("#equations").append(
		"<p>" + generateRandomEquation() + "</p>"
		);
});
;

let userAnswer = document.getElementById("#result")

function comparison(userAnswer, resultOut){
	if (userAnswer === resultOut){

	}

}
