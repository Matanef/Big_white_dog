//function

//DEFINE A FUNCTION, CREATE A FUNCTION
function makeChocolate (){
	console.log("hello, we are making chpcplate")
	//statement
}

//INVOKE THE FUNCTION, CALL THE FUNCTION
makeChocolate();

//dark: 80g
//milk: 60g

//parameter: makeChocolateWithGrams (**this one**)

function makeChocolateWithGrams (addonChocolate){
	let gramsOfChocolate = 50;
	let totalGramsOfChocolate = gramsOfChocolate + addonChocolate;
	console.log(`The totalGramsOfChocolate is ${totalGramsOfChocolate} grams`)
}
// makeChocolateWithGrams();



function makeChocolateWithGrams (typeChocolate,addonChocolate){
	let gramsOfChocolate = 50;
	let totalGramsOfChocolate = gramsOfChocolate + addonChocolate;
	console.log(`The totalGramsOfChocolate from ${typeChocolate} is ${totalGramsOfChocolate} grams`)
}
makeChocolateWithGrams("dark", 30);
makeChocolateWithGrams("milk", 10);

let shoppingCartJohn =[]
{
	product:"pen"
	price: 10
}
{
	product: "table"
	price: 50
}
{
	product:"printer"
	price:120
}
{
	product:"phone"
	price:2000
}

function sumShoppingCartPrice (shoppingCart) {
	let sumPrice = 50
	for (let item of shoppingCart){
		let priceItem = item["price"];
		sumPrice += priceItem
	}
	
	// console.log(priceItem)
	console.log(`${sumPrice}`)
}

sumShoppingCartPrice(shoppingCartJohn)
// let shoppingCartJohn =[]
// {
// 	product:"pen"
// 	price: 10
// }
// {
// 	product: "table"
// 	price: 50
// }
// {
// 	product:"printer"
// 	price:120
// }
// {
// 	product:"phone"
// 	price:2000
// }



//Local Scope
	//block scope

//gobal scope
// let age = 23;
// //if i create a variable in the global scope
// //i can access it in the local scope

// function calculateAge(){
// 	console.log(age); //3rd line executed
// 	age *= 2; //4th line to execute
// 	console.log(age); //5th line to execute
// }
// console.log(age); //1st consol.log// 20
// calculateAge();//2nd line executed
// console.log(age); //6th line to be executed

// function calculateAge (){
// 	let age =23
// }

// calculateAge();
// //if a variable was creatd oin the local scope 
// //it does not accessible in the global scope
// console.log(age);

// //block scope:
// // if statement
// //loop

// let age =12 
// if (age <= 12){
// 	console.log(age);
// 	let canParty = false;
// }
















// function calculatreAge(){
// 	//local variable
// 	let age = 23
// 	return = age
// 	//let name ="David" // won't  be executed
// }

// // the return keyword means:
// // now the function has a result - age - 23

// let value = calculatreAge();

// calculatreAge();

// //global scope
// // console.log(age); //undefined since we are trying to reach a local
// //scope from local scope

// // We have a local variable
// // 



// // global variable
// let prices = [23, 54, 12];

// function sumPriceRestaurant(){
// 	let sum = 0
// 	for (let p of prices){
// 		sum+= p;
// 	}
// }

// //find the sum included Taxes
// function sumPriceRestaurantWithTaxes(){
// 	//console.log(sum); // this will return an unidentified
// 	let sumPrices = sumPriceRestaurant();
// 	let sumPricesWithTaxes = sumPrices * 1.17;
// }

// sumPriceRestaurantWithTaxes();

// if i have a local variable declared in a function and i want
//to use it in another functionod in the global scope

//1. i need to return the value in the first function
//2. i need to 



let colors = ["blue", "lightred", "red"];

// we want to display everyletter of every color

// Function - takes no parameter
// for of - for with index
function spellingGame (){
	for (let col of colors) {
		console.log(col)
		for (let i =0; i < col.length; i++){
			console.log(col[i])
		}
	}
}
spellingGame();

//1st loop
//col = blue
//length of the word = 4

	//1st nested loop
	//col[i] -> clo[0] -> "blue[0" -> b

	//2nd nested loop
	//col[i] -> clo[1] -> "blue[1]" -> b
	
		//3rd nested loop
	//col[i] -> clo[2] -> "blue[2]" -> b

		//4th nested loop
	//col[i] -> clo[3] -> "blue[3]" -> b