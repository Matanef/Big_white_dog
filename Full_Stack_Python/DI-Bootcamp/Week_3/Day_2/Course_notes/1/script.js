// function playTheGame(){
// 	alert("let's play")
// }

// playTheGame()

// addEventListener

// 1. Retrieve the button

// let buttonToClick = document.getElementById("btn");
// let buttonToClick = document.querySelector("#btn");

// get all the paragraphs
// let allParagraphs =  document.querySelectorAll("div p")


// addEventListener

// 1. Retrieve the button
let buttonToClick = document.querySelector("#btn");

// 2. Add an event listener to it
// element.addEventListener(typeEvent, callbackfunction);

buttonToClick.addEventListener("click", sayHelloClick)
buttonToClick.addEventListener("mouseover", sayHelloHover)

function sayHelloClick () {
	console.log("Hello CLICK")
}

function sayHelloHover () {
	console.log("Hello HOVER")
}

// Retrieve the h1
let title = document.getElementById("title");

title.addEventListener("click", sayHelloClickH1)

function sayHelloClickH1 () {
	console.log("Hello CLICK")
}


// Retrieve the 2 buttons

let buttonBlueOne =  document.getElementById("btn-blue-one");
let buttonRedOne =  document.getElementById("btn-red-one");


// // functions
function changeBackgroundToBlue () {
	document.body.style.backgroundColor = 'blue';
}

function changeBackgroundToRed () {
	document.body.style.backgroundColor = 'red';
}

// // addeventlistener

buttonBlueOne.addEventListener("click", changeBackgroundToBlue)
buttonRedOne.addEventListener("click", changeBackgroundToRed)

// With more buttons
let buttonBlueTwo =  document.getElementById("btn-blue-two");
let buttonRedTwo =  document.getElementById("btn-red-two");
let buttonYellowTwo =  document.getElementById("btn-yellow-two");


// function --- the parameter is called the event object
// we call the event object using a letter "e" but we can call
// it whatever we want - 
//the event object is an js object that contains information about the event that occured
function changeBackground (e) {
	console.log(e);
	console.log(e.target);

	// with the style
	let styleBtn = window.getComputedStyle(e.target).backgroundColor;
	document.body.style.backgroundColor = styleBtn;

	// with the text
	// let textBtn = e.target.textContent.toLowerCase();
	// document.body.style.backgroundColor = textBtn;

	// document.body.style= `background-color : ${textBtn}; border:5px solid white `;
}

// addeventlistener

buttonBlueTwo.addEventListener("click", changeBackground);
buttonRedTwo.addEventListener("click", changeBackground);
buttonYellowTwo.addEventListener("click", changeBackground)