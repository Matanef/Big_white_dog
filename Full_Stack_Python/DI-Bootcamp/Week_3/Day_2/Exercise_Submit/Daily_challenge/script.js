let button = document.getElementById("lib-button");
let userInput = [];

function madLib(){
	let inputElement = document.querySelectorAll("input");
	for (let i = 0; i < inputElement.length; i++){
		userInput.push(inputElement[i].value);
	}
	let sentence = document.getElementById("story");

	sentence.textContent = `${userInput[2]} is ${userInput[1]} in ${userInput[4]}. He is ${userInput[3]} with a ${userInput[0]}`
}

button.addEventListener("click", madLib);