function calculateTip() {
	let amountOfBill = parseInt(prompt(`What is the bill amount?`))
	if (amountOfBill < 50) {
		console.log(`the Tip sum is ${amountOfBill*0.2} and the total sum including the Tip is ${amountOfBill+(amountOfBill*0.2)}`)
	}else if (50 > amountOfBill && amountOfBill <= 200){
		console.log(`the Tip sum is ${amountOfBill*0.15} and the total sum including the Tip is ${amountOfBill+(amountOfBill*0.15)}`)
	}else {
		console.log(`the Tip sum is ${amountOfBill*0.1} and the total sum including the Tip is ${amountOfBill+amountOfBill*0.1}`)
	}
}

calculateTip()