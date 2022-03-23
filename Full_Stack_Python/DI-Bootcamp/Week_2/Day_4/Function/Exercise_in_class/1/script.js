let ageArr = []
{
	own : 37
	mum : "own"*2
}
{
	dad : "mum"*1.2
}


// function myAge() {
// 	for (let key in ageArr){
// 		console.log(`${key} ${ageArr[key]}`)
// 		console.log(ageArr[key])

// 		// for (let diffAge in ageArr)
// 		// 	console.log(ageArr)
// 	}

// 	myAge()



// create a function - parameter
function calculateAge (myAge){
	let ageMum = myAge*2;
	let ageDad = ageMum*1.2;
	console.log(`The Age of my Dad is ${ageDad} The age of my mum is ${ageMum}`)
}

//call a function - argument
calculateAge(30)