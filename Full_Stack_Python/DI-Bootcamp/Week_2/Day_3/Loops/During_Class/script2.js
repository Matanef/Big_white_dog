// for (let counter = 0; counter <=6; counter ++){
// 	console.log("hello");
// }

// let animals = ["cow", "hen"];
// for (let i = 1; i <= 3 ; i++){
// 	let userAnimal = prompt("What animal do you want to add ?");
// 	animals.push(userAnimal)
// }

// console.log(`The Animals are ${animals}`)
// {
// 	username:"Jane"
// 	age: 22
// 	levelGame: 19
// 	isGoodPlayer: true
// 	products: ["gun", "chain"],
// }
// {
// 	username:
// 	age
// 	levelGame:
// 	isGoodPlayer:
// 	products: ["dog", "arrow"],
// }
// ];


// for (let i = 0; i < players.length; i ++){
// 	players[i]["game"] = "ABC"
// }


// let colors = ["red", "black", "white"]

// for (let i=0; i < colors.length; i++ )
// 	console.log(colors[i]);

// for (let favorite of colors){
// 	console.log(favorite)
// }
// let players = [
// {
// 	username:"Jane",
// 	age: 22,
// 	levelGame: 19,
// 	// isGoodPlayer: true
// 	// products: ["gun", "chain"],
// },
// {
// 	username:"Marc",
// 	age: 45,
// 	levelGame: 39,
// 	// isGoodPlayer: false
// 	// products: ["dog", "arrow"],
// }
// ];

// //FOR OF LOOP

// for (let player of players){
// 	player["game"] ="ABC"
// }
// console.log(players)


//WHILE LOOP

let bankAmount = 10000;
let computerPrice = 2000;
let howManyComputerBought = 0;
console.log(`i have ${bankAmount} shekels in my account`);
console.log(`i havei now have ${howManyComputerBought} computers`)

//do i have enoughtmoney to buy a computer
while (bankAmount >= computerPrice) {
	bankAmount -= computerPrice;
	howManyComputerBought ++;
	console.log(`i have ${bankAmount} shekels in my account`);
	console.log(`i havei now have ${howManyComputerBought} computers`)


	if (bankAmount < computerPrice) {
		console.log(`END GAME: i have ${bankAmount} shekels in my account`);
		console.log(`i don't have enough money left`)
	}
}



let userLanguage = prompt("what is your Language?")

if (userLanguage === "French") {
	alert("Bonjour")
} else if (userLanguage === "English") {
	alert("Hello")
} else if (userLanguage === "Spanish") {
	alert("Hola")
}else {
	alert("bye")
}

switch(userLanguage){
	case "French":
	alert("Bonjour")
	break;
	case "English"
	alert("Hello")
	break;
	case "Spanish"
	alert("Hola")
	break;
	default:
	alert("Bye")
}