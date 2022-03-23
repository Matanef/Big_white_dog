function isDivisible(){
	let sum = 0
	for (let i= 0; i <= 500; i++){
		
		let divis = i % 23;
		if (divis == 0) {
			console.log(i)
			sum+=i;

		}
		

	}
	console.log('The sum:', sum);
}
isDivisible();

