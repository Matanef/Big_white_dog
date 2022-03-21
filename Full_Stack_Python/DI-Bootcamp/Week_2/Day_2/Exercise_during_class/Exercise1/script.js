drive = 18


let driverAge = prompt("please enter your age")

if (driverAge < drive) {
	console.log("Sorry, you are too young to drive this car. Powering off");
} else if (driverAge == drive){
	console.log("Congratulations on your first year of driving. Enjoy the ride!");
}else if (driverAge > drive){
	console.log("Powering On. Enjoy the ride!")
}

