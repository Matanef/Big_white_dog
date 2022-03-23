// let change = []
// {
// 	quarters: 0.25
// }
// {
// 	dimes: 0.10
// }
// {
// 	nickel: 0.05
// }
// {
// 	penny: 0.01	
// }

function changeEnough(itemPrice, amountOfChange){
	let wallet = 0;
	let coins = [0.25, 0.1, 0.05, 0.01];
	// for (let item of amountOfChange) {
	// 	wallet += Number(amountOfChange[item]) * Number(coins[item]);
	for (let i = 0; i < amountOfChange.length; i++) {
		wallet += Number(amountOfChange[i]) * Number(coins[i])
	}
	if (wallet >= itemPrice){
		return true;
	}


	return false;
}

let c = changeEnough(4.25, [25,20,5,0]);
console.log(c);