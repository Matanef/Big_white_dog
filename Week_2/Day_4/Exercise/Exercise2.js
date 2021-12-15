function calculateTip(){
	let billAmount = parseInt(prompt("Bill Amount"))
		if (billAmount < 50) {
		return `the tip should be ${billAmount*0.2}`
		} else if (billAmount> 50 , billAmount <200){
			return `the tip should be ${billAmount*0.15}`
		} else if ( billAmount > 200) {
			return `the tip should be ${billAmount*0.10}`
		}

console.log(billAmount)

}
let billamoutout = parseInt(calculateTip(billAmount));

console.log(billamoutout)

calculateTip()




// console.log(`the final amount is `${billAmount} + calculateTip());