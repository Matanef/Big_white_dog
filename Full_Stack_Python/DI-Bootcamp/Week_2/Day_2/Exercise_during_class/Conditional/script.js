// let bankAmount = 10000;
// let computerPrice = 8000

// let phonePrice = 4000
// let breadPrice = 10

//currently true
if (bankAmount > computerPrice) {
	console.log("I'll buy the computer");
	bankAmount = bankAmount - computerPrice;
	console.log(`I have ${bankAmount} shekels left in my account`)
			//	= 10000 - 8000
	//if the condition above is false
}else {
	console.log("i will buy a phone");
}





if (bankAmount >= computerPrice){
	console.log("i'll buy a computer")
} else if (bankAmount >= phonePrice) {
	console.log("I'll buy a phone")
} else{
	console.log("I'll buy a bread")
}
console.log("OUT")

// if (condition is true) {
// }else if(condition above is false, and condition here is true){

// }else if(condition above is false, and condition here is true){

// }else if(condition above is false, and condition here is true){
// 
// }else if(condition above is false, and condition here is true){

// }else{

// }

// let bankAmount = 10000;
// let computerPrice = 8000
// let computerColor = "blue"

// if (bankAmount >= computerPrice && computer ==="blue");{
// console.log("Ill buy a computer")
// else if (computerColor !=="blue")}{
// 	console.log("I'll buy a red computer")
// }else {
// 	console.log("nothing")
// }

// if (bankAmount >= )


let players = [
{
	username: "Jane",
	age: 22,
	levelGame: 15,
	isGoodPlayer: true,
	products : ["gun", "cat", "uniform"]

};

//is the level game of player  is bigger than 20 -> I 
//want to add inside the object.
//a property is GoodPlayer = true
//is between 50 not included and 15 included -> middle
// else bad

if (player["levelGame"] >= 50){
	player["isGoodPlayer"] = true;
} else if (player["levelGame"]  >= 15 && player["levelGame"]  <= 50) {
	player["isGoodPlayer"] = "middle";
} else {
	player["isGoodPlayer"] = "false"
}
