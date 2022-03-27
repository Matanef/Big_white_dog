// Create 3 pictures on the page, each of them with a random
// source image

let pics = [
"https://idsb.tmgrup.com.tr/ly/uploads/images/2021/09/08/thumbs/800x531/142774.jpg",
"https://spca.co.il/wp-content/uploads/2021/11/dog.jpeg",
"https://i1.sndcdn.com/avatars-000570452091-updhur-t500x500.jpg"
];

// display them dynamicaly on the page

// Retrieve where we want to add the images
let section = document.getElementById("game");

function createImg(){

	for (let i = 0; i<pics.length; i++){
		let randomNumber = Math.floor(Math.random() * pics.length);
		// create an img
		let newImg = document.createElement("img");
		newImg.classList.add("animals");
		newImg.setAttribute("src", pics[randomNumber]);
		//append the image on the section
		section.appendChild(newImg);
	}
}

createImg();