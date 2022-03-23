// function hotelCost() {
// 	let night;
// 	do {
// 		night = prompt(`how many nights?`)
// 		console.log(night);
// 	}
// 	while (isNaN(night)||night=='')
// 		return night*140
// }
// let total = hotelCost();
// console.log(total);


function planeRideCost(){
	let dest;
	do {
		dest = prompt(`Where to?`)
		console.log(dest);
	}
	while (!Number.isFinite(dest)||dest=='')
		return dest
}

planeRideCost()
// let a = planeRideCost();
// console.log(a);