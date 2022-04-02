	

function volumeOfSphere(){
	let volume;
	let radius = document.getElementById("radius").value;
	// for (let i = 0; i=2; i++ ){
	// 	let radiusHigh = radius[i];
	let volume = 4/3 * Math.PI * Math.pow(radius, 3);
	

	return volume

}
let volume = volumeOfSphere()
console.log(volume)
