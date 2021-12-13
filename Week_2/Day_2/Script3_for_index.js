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
// 2. Change the price of the pear, so it will contain the Taxes. 17%
// 3. Ask the user for the fruit he wants between Apple, Banana and Pear.
// Make sure that your code accept all type of strings,
// for example "Banana" or "banana" or "BaNaNA"
// 4. Console.log the price for the specific fruit the user wants




//1 
userCart["lastNameBuyer"] = "Smith";
console.log(userCart)


userCart["prices"]["pear"] *=1.17;
console.log(userCart)

let Fruit = prompt("Please Select a Fruit: Banana, Apple, Pear").toLowerCase
console.log(Fruit)

let PriceForSpecificFruit = userCart["prices"][Fruit]
console.log("PriceForSpecificFruit : ", PriceForSpecificFruit)
//console.log(the Price of a ${Fruit} is ${PriceForSpecificFruit})




//Solution:

