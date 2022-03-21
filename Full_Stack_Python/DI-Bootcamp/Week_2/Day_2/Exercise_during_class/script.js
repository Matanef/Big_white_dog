// // Exercise

let a = 2
		//it's previous + 3
		a= a+3
		console.log(a);
		//Shortcut
		a += 3
		console.log(a);


		let b = 5;
		b = b *2;
		console.log(b);

		b *= 2
		console.log(b);

		let c = 3
// 1st possibility
c = c + 1
console.log(c);
//2nd possibility
c += 1;
console.log(c);
//3rd possibility
c ++
console.log(c);


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

userCart["lastName"]="Smith";
console.log(userCart)

userCart.prices["pear"]=0.2*.17;
console.log(userCart);

userCart["prices"]["pear"] *=1.17;
console.log(userCart);


// let userFruit = prompt("what fruits do you want: Apple Banana or Pear");

// let userFruitLower = userFruit.toLowerCase();
// console.log(userFruitLower)


let userFruit = prompt("what fruits do you want: Apple Banana or Pear").toLowerCase();
console.log(userFruit);

// console.log(userCart["prices"]["apple"]);
// console.log(userCart["prices"]["banana"]);
// console.log(userCart["prices"]["pear"]);

// console.log(userCart["prices"][userFruit]);
// //								"apple"
// //								"pear"
// console.log(`${userCart["prices"].userFruit}`);

console.log(userCart["prices"][userFruit]);



