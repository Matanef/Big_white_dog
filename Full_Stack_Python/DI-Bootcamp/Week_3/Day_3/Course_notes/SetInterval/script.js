// // setInterval
let section = document.getElementById("container")
let button = document.getElementById("btn")

button.addEventListener("click", stopAnimation)

function addDiv(){
	let div = document.createElement("div");
	let text = document.createTextNode("hello");
	div.appendChild(text);
	section.appendChild(div);
}
let timeId = setInterval(decreaseNumber, 1000);
let spanTime = document.getElementById("time");
let counter = 10;

function decreaseNumber (){
	if (counter >= 0) {
		spanTime.textContent = counter;
		counter --;
	} else {
		spanTime.textContent = "DONE";
		clearInterval(timeId);
	}
}