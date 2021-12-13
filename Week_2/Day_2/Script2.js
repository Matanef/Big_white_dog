//-----------Part I ---------------

// array  : list of elements
//ordered list
let shopping = ["shampoo", ["chocolate", "vanilla"], ["paper", "pen"]]

//object
//key :value pair
//key :value pair
// {
	//key: value
	//key : value
	//key : value
//}

let shopping = {
	apple: 2,
	pears: 4,
	banana:5,
	isShampooavailable: true
	usernameBuyer: "john",
	coupons : ["12$", "14$"],
};

console.log(shoppingObj)

//objectName.propertyName
console.log("how many apples I need to buy ", shoppingObj.apple)

//
console.log("how many apples I need to buy ", shoppingObj["apple"])

//Value of the second coupon
console.log(shoppingObj["coupons"][1])

//change the value of a key
shoppingObj["usernameBuyer"] = "Thomas";
console.log(shoppingObj)

//change the value of a key
shoppingObj["LastnameBuyer"] = "Smith";
console.log(shoppingObj)






// ------------ PART I ----------------

// array : list of elements
// ordered list
// indexed list
let shopping = ["shampoo", ["chocolate", "vanilla"], ["paper", "pen"]];

//change the value of an element inside the array
shopping[0] = "computer";

//object
// key : value pair
// key: value pair
// {
// 	key : value,
// 	key : value,
// 	key : value,
// }

let shoopingObj = {
	apple: 2,
	pears: 4,
	banana: 5,
	isShampooAvailable: true,
	usernameBuyer: "John",
	coupons : ["12$", "14$"]
};

console.log(shoopingObj)

// objectName.propertyName
console.log("how many apples I need to buy ", shoopingObj.apple)

// objectName["propertyName"]
console.log("how many apples I need to buy ", shoopingObj["apple"])

//value of the second coupon
console.log(shoopingObj["coupons"][1])

//change the value of a key
shoopingObj["usernameBuyer"] = "Thomas";
console.log(shoopingObj)

//add a new key:value pair
shoopingObj["lastNameBuyer"] = "Smith";
console.log(shoopingObj)



let family = {
	lastname : "Smith",
	members : 4,
	hasADog : true,
	nameOfMembers : ["Lea", "David", "Mom", "Dad"],
	friends : {
		name : "Jack",
		lastname : "ABC",
		age : 12,
		favoriteColors : ["blue", "red"],
	}
};

//1. Retrieve the number of the members of the family
console.log(`There are ${family.members} members in the family`)
console.log(`There are ${family["members"]} members in the family`)

//2. Retrieve the name of Lea
// positionLea = 3
// --> she would be the 4th member

// positionLea = 0
// --> she would be the 1th member
let positionOfLea = family["nameOfMembers"].indexOf("Lea");
console.log("index of Lea in the array : " , positionOfLea)
console.log(`The ${positionOfLea+1}# member of the family is Lea`)


// Find the age of my friend
console.log(`The age of my friend ${family.friends.name} is ${family.friends.age}`)
console.log(`The age of my friend ${family["friends"]["name"]} is ${family["friends"]["age"]}`)