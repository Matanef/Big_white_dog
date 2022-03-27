
// // retrieve the body
// let body = document.body;

// //retrieve navbar
// let navbar = document.body.children

let pics = [
"pexels-pixabay-39317.jpg",
"pexels-pixabay-45201.jpg",
"pexels-pixabay-47547.jpg",
"pexels-pixabay-219906.jpg"
]


//display dynamicaly on page
//retrieve where we want to add the imgs
let section = document.getElementById("game");


function createImg(){
	for (let i=0; i<pics.length; i++){
		let randomNumber = Math.floor(Math.random() * pics.length);
// create an img object
let newImg = document.createElement("img");
newImg.classList.add("animals");
newImg.setAttribute("src", pics[randomNumber]);
//append the image on section
section.appendChild(newImg);

}
newImg.classList.add("animals");
}
createImg();