// let userNumber = prompt("Please enter a number");
// let userInt = parseInt(userNumber)
// console.log(typeOf(userInt));

// for (let i = userInt; i < 10;){
// 	console.log(`small number ${userNumber} and loop will continue`)

// 	if(i > 10){
// 		break
// 	}else {
// 		let userNumber = prompt("Please enter a number");
// 		let userInt = parseInt(userNumber)


// 	}
// }
// do{
// 	console.log(`small number ${userNumber} and loop will continue`)

// }
// while (userInt < 10)



// while (userNumber<10){
// 	console.log(`User selected the number ${userNumber} and it is lower then 10, resuming loop`);
	// userNumber++

// } 
let userInt = 0
while (userInt < 10){
	let userNewNum = prompt("Please enter a number");
	if(!isNaN(userNewNum)){
		userInt = Number(userNewNum)	
		console.log(`user selected ${userInt}`);

		if(userInt > 10){
			break;
		}
	}
}