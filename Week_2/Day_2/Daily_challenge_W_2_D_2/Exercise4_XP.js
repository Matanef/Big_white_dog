let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
//since the exercise mentioned that all the above users are already online we can use 
//the length command the count the amount of elements in the array:
let length = users.length;
console.log(users.length)
console.log(users)


if (length == 0) {
	console.log("no one is online")
} else if (length == 1) {
	console.log(`${users} has come Online`)
} else if (length == 2) {
	console.log(`${users} are Online`)
} else if(length >=3) {
	console.log(`${users [0]} , ${users [1]} and 2 more users are connected`)
}
