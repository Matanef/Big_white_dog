// let title = document.getElementById("title");
// console.log(title)

// 1. Array from the instruction
let colors = ["blue", "yellow", "green", "pink"];

// 4.2 - the changeBackground function
// The changeBackground function receives automatically the event object from
// the addEventListener method
// the name of the parameter doesn't matter - but usually we call it
// e or evt or event
// the event object object holds information about the event 
function changeBackground (evt) {
	console.log(evt) 
	// 4.3 : I need to retrieve the text content of the button
	// To retrieve the text content of the button, 
	// first, I need to retrieve the button that was clicked : evt.target
	// then, I retrieve the text content the button that was clicked : evt.target.textContent
	let textBtn = evt.target.textContent;
	// 4.4 - I need to change the backgroundColor of the body to the textContent of the button
	// I select the background color of the body and make it equal to the textContent of the button
	document.body.style.backgroundColor = textBtn;
}

// 3. Create a button of each color, and append them to the container div
// To answer this instruction, we do a function, 
// because code need to be wrapped inside a function

function createButtons(){
	// 3.1 - retrieve the div container from the DOM
	let container = document.getElementById("container");

	// 3.2 - If I have an array of color, and I want to create one button per color
	// I can use a loop - the loop runs x times. 
	// x being the length of the colors array - 1
	for (let i = 0; i<colors.length; i++){
		// 3.4 - create a button using the createElement method
		let newButton = document.createElement("button");
		// 3.5 - each button needs to have a text - we use the textContent property
		// and the value should be the color  :  colors[i]
		newButton.textContent = colors[i];

		// 3.6 - each button needs to have a background color 
		// - we use the style property, more specifically the backgroundColor property
		// and the value should be the color  :  colors[i]
		newButton.style.backgroundColor = colors[i];
		
		// 3.7 - each button needs to be appended to the container
		// we use the appendChild method
		container.appendChild(newButton);

		// 4 - Each button should have an "click" event listener 
		// that changes the background color of the document, 
		// to the textcontent of the button (do it directly in the JS)

		// 4.1 - each button has an event listener, that listens to a "click" event
		// in the addEventListener we add the type of event "click"
		// and the function that should be called when the click event happens
		// everytime we click on a button, it calls the changeBackground function
		newButton.addEventListener("click", changeBackground);
		
	}
}




createButtons()