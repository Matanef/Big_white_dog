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

// 1. If the user is SignedIn - show him his name and password
// 2. If not - alert the user "you need to sign in"
if (userCart["isUserSignedIn"]){
	alert(`Your username is ${userCart["username"]} and your password is ${userCart["password"]} `)
} else {
	alert("You need to sign in")
}

// 3rd exercise
//  1. If the user is Johnny AND his password is 12345 - alert him "You are signed in"
//  2. If the user is not Johnny OR his password is not 12345 - alert him "One credential is false"
//  3. Else, alert the user "you need to sign in"

if (userCart["username"] == "Johnny" && userCart["password"] == 12345 ) {
	console.log("You are signed in")
} else if (userCart["username"] == "Johnny" || userCart["password"] == 12345) {
	console.log("One credential is false")
} else {
	console.log("you need to sign in")
}