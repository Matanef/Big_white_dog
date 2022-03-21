//premitive data types
// -String, Number, Boolean

// let players = [["Jane", 22, 15], ["Marc", 45, 77]]

//Objects - curly brackets

// let x = {
// 	property: value;
// 	property: value;
// 	method: function
// }

// let player = {
// 	username: "Jane",
// 	age: 22,
// 	levelGame: 15,
// 	isGoodPlayer: true,
// 	products : ["gun", "cat", "uniform"]

// }

// console.log(player["products"])

// Syntax: nameOfObject.nameOfProprty
// let namePlayer = player.username;

// let namePlayerOne = player ["username"];

// console.log(`the username of the player is ${namePlayer}`);
// console.log(`the username of the player is ${namePlayerOne}`);

// let levelPlayer = player["levelGame"];
// console.log(`The level of the player is ${levelPlayer}`)


// let productsPlayer = player["products"][1];
// console.log(productsPlayer)

// //access the letter "u" from the "gun"
// let letter = player["products"][0].charAt(1);
// console.log(letter);

//player["products"][0][1];


//Jane leveled up, need to update the player level

// player["levelGame"]=20
// console.log(player)

// //if the property does not exist in the object the following will ADD
// //it and assign a value to it.

// player["lastName"]="Smith";
// console.log(player)

let players = [
{
	username: "Jane",
	age: 22,
	levelGame: 15,
	isGoodPlayer: true,
	products : ["gun", "cat", "uniform"]

},
{
	username: "Marc",
	age: 45,
	levelGame: 95,
	isGoodPlayer: true,
	products : ["dog", "arrow"],

}
]

let playerTwo = players[1];
console.log(playerTwo)

let ageMarc = players[1];
console.log(ageMarc);