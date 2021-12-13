// Exercise

let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

// 1. Add the lastname Smith to the object
userCart["lastname"] = "Smith";
console.log(userCart)

// 2. Change the price of the pear, so it will contain the Taxes. 17%
// userCart["prices"]["pear"] = userCart["prices"]["pear"]*1.17
userCart["prices"]["pear"] *= 1.17
console.log(userCart)

// 3. Ask the user for the fruit he wants between Apple, Banana and Pear.
// Make sure that your code accept all type of strings,
// for example "Banana" or "banana" or "BaNaNA"
let answerUser = prompt("Which fruit do you want: Apple,Banana,Pear").toLowerCase()
console.log(answerUser)
// "banana" == "BaNAna" 
// false

// 4. Console.log the price for the specific fruit the user wants
// let priceForSpecificFruit = userCart.prices.answerUser
// dot notation doesn't work with variables
// line 120 not working
let priceForSpecificFruit = userCart["prices"][answerUser];
//if the answer is apple, 
// userCart.prices.answerUser
// userCart.prices.apple
//if the answer is pear, 
// userCart.prices.answerUser
// userCart.prices.pear
console.log("priceForSpecificFruit : ", priceForSpecificFruit)
console.log(`The price for a ${answerUser} is ${priceForSpecificFruit}`)


// // Exercise

let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5,
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

// 1. Add the lastname Smith to the object
userCart["lastname"] = "Smith";
console.log(userCart)

// 2. Change the price of the pear, so it will contain the Taxes. 17%
// userCart["prices"]["pear"] = userCart["prices"]["pear"]*1.17
userCart["prices"]["pear"] *= 1.17
console.log(userCart)

// 3. Ask the user for the fruit he wants between Apple, Banana and Pear.
// Make sure that your code accept all type of strings,
// for example "Banana" or "banana" or "BaNaNA"
let answerUser = prompt("Which fruit do you want: Apple,Banana,Pear").toLowerCase()
console.log(answerUser)
// "banana" == "BaNAna" 
// false

// 4. Console.log the price for the specific fruit the user wants
// let priceForSpecificFruit = userCart.prices.answerUser
// dot notation doesn't work with variables
// line 120 not working
let priceForSpecificFruit = userCart["prices"][answerUser].toFixed(2);
//if the answer is apple, 
// userCart.prices.answerUser
// userCart.prices.apple
//if the answer is pear, 
// userCart.prices.answerUser
// userCart.prices.pear
console.log("priceForSpecificFruit : ", priceForSpecificFruit)
console.log(`The price for a ${answerUser} is ${priceForSpecificFruit}`)