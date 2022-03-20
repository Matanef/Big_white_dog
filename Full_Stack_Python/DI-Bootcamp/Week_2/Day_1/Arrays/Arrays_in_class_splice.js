// // let	addressNumber
// // addressNumber = 19;
// let	addressNumber = 19

// // let addressStreet
// // addressStreet = "Nitzana";
// let addressStreet = "Nitzana"

// // let country
// // country = "israel";
// let country = "israel"

// let globalAddress = `i live in the ${addressNumber} ${addressStreet} ${country} `

// // console.log (globalAddress)

// let ownbirth = 1984
// let futuredate = 2038

// let result = ` i will be at the age of ${futuredate - ownbirth}`
// console.log (result)

// let shoppingItems = ["shampoo", "chocolate", "pen"];

// let exampleArray = ["shampoo", 3, true];

// let firstItem = shoppingItems[0];
// let thirdItem = shoppingItems[2];

// console.log(firstItem);
// console.log(thirdItem);
// console.log(shoppingItems.length);


// // adding items to array

// let jewlery = ["diamond", "bracelet"];
// console.log(jewlery);

// jewlery.push("necklece");
// console.log(jewlery);

// pop remove th e last item

// let shoppingCart = ["shampoo", "chocolate", "pen"];
// console.log(shoppingCart)

// shoppingCart.pop()
// console.log(shoppingCart)

//elete
//Splice
//nameOfTheArray.splice (where i want to start deleting/adding, 
// how many elements o want to remove, new elements to add)
// shoppingCart.splice(1, 1)
// console.log(shoppingCart)


// let shoppingCart = ["shampoo", "chocolate", "pen", "vanilla", "computer"];
// console.log(shoppingCart);
// //delete "chocolate, pen & vanila and add "water" instead

// shoppingCart.splice(1, 3, "water");
// console.log(shoppingCart)


//find the position of an element
let jewlery = ["diamond", "bracelet", "necklace"];

//Syntax: nameOfArray.indexOf ("the item")
let positionBracelet = jewlery.indexOf("bracelet");
console.log(positionBracelet);
console.log(jewlery);

jewlery.splice(positionBracelet, 1);

console.log(jewlery);

//the same
jewlery.splice(jewlery.indexOf("bracelet"), 1)

console.log(jewlery)

// 	EQUALS
let age = 10 //1 equalmeans "assigning"; 1 add the 
//				value 10 to the variable age
1==10 // 2 equals are comparing
1===1 //3 equals means comparing the value and the type
1 === "1" //false