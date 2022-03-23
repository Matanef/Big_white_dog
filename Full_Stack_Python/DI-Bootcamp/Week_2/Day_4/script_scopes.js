/ global scope
// global variable
let age = 20;

// // If I create a variable in the global scope
// // I can access it in the local scope
function calculateAge () {
	console.log(age); //3rd line executed //20
	age *= 2; //4th line to execute
	console.log(age); //5th line to execute //40
}

console.log(age); //1st console.log //20
calculateAge(); //2nd line executed 
console.log(age); //6th line to execute //40


// local scope
// function scope
function calculateAgeOther() {
	// local variable
	let age = 23;
}

calculateAgeOther();
// if a variable was created in the local scope, 
// it's not accessible in the global scope
console.log(age); //undefined

// Global Scope

// ---

// Local Scope
// 	Function Scope - function
// 	Block Scope - if, switch, for, while

// If a variable is declared in the global scope
// it is accessible in the local scope

// If a variable is declared in the local scope
// it is NOT accessible in the global scope

let colors = ["blue", "red", "green"];

// // local scope
for (let favorite of colors) {
	console.log(favorite)
}

// // global scope
console.log(favorite); //undefined

let age = 12;

if (age <= 12) {
	console.log(age); //12
	let canParty = false;
}

console.log(canParty) //undefined

// ------------------- RETURN

// We have a local variable
// We want to access it inside the global scope


function calculateAge() {
	// local variable
	let age = 23;
	return age;
	// let name = "David" //won't be executed
}


//the return keyword means : 
//now the function has a result - age - 23

let value = calculateAge(); //the variable value is now equal to 23

// EXAMPLE

// global variable
let prices = [23, 54, 12];

// find the sum of the prices
function sumPriceRestaurant (){
	let sum = 0;
	for (let p of prices) {
		sum += p;
	}
	return sum;
}


// find the sum included Taxes
function sumPriceRestaurantWithTaxes (){
	// console.log(sum); //undefined
	let sumPrices = sumPriceRestaurant();
	let sumPricesWithTaxes = sumPrices * 1.17;
}

sumPriceRestaurantWithTaxes();



//If I have a local variable declared in a function
//and I want to use it in another function
//or in the global scope

// 1. I need to return the value in the first function
// 2. I need to call the first function inside the second function