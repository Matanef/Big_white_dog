//1. Retrieve the button
let button = document.getElementById("lib-button");
let listWords = [];

// 3. Function retrieveData
function retrieveData(){
	// 3.1 - before we retrieve the data from the inputs, we need to retrieve
	// the inputs
	let allInputs = document.querySelectorAll("input");

	// 3.2 - to retrieve the values from the inputs, I need to loop through the inputs
	// and retrieve their value
	for(let i=0; i<allInputs.length;i++){
		// 3.3 - to retrieve the value from an input we use element.value
		// 3.3 - retrieve the value of every input and push each of them
		// to the array listWords
		listWords.push(allInputs[i].value);
	}
	// 3.4 - display the sentence on the page
	// retrieve the span that in inside the HTML file
	let span = document.getElementById("story");
	// we use element.textContent to add a text to the span
	span.textContent = `${listWords[2]} is ${listWords[1]} in ${listWords[4]}. He is ${listWords[3]} with a ${listWords[0]}`
}

// 2. Add the button a click event listener
//when we click on the button we call the function retrieveData
button.addEventListener("click", retrieveData);