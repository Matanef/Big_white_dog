function welcomeUser () {
	let section = document.getElementById("container");
	let newDiv = document.createElement("div");
	newDiv.classList.add("box");
	let textDiv = document.createTextNode("Welcome new user");
	newDiv.appendChild(textDiv);

	section.appendChild(newDiv);
}

setTimeout(welcomeUser, 2000);



function welcome (){
	document.body.style.backgroundColor = "red";
	setTimeout(getBlue, 2000)
}

function getBlue(){
	document.body.style.backgroundColor = "blue";
}

setTimeout(welcome, 2000);