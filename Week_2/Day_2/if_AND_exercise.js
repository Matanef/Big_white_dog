let userCart = {
	username : "Johnny",
	password: 12345,
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

if (userCart["isUserSignedIn"]) {
	alert(`Your username is ${userCart["username"]} and your password is ${userCart["password"]}`)
} else {
	alert("You need to sign in")
}