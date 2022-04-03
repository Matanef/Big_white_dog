let submitForm = document.getElementById("submit")
submitForm.addEventListener("click", volumeOfSphere)

function volumeOfSphere(){
	event.preventDefault()
	let radiusValue = document.getElementById("radius").value;
	// for (let i = 0; i=2; i++ ){
	// 	let radiusHigh = radius[i];
	let equation = 4/3 * Math.PI * Math.pow(radiusValue, 3);
	let volumeres = document.getElementById("volume");
	volumeres.value = equation


}