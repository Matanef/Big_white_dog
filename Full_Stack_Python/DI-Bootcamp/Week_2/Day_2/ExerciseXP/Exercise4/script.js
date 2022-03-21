let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000", "e", "g"];
let userslength = users.length;
console.log(userslength)

//i added "e" and "g" just to check if the code works


if (userslength === 0){
	console.log("no one is online")
}else if (userslength === 1){
	console.log(users[0])

} else if (userslength === 2) {
	console.log(users[0], users[1]);

}else if (userslength > 2) {
	console.log(users[0], users[1], `more ${userslength-2} users are online`);
}
