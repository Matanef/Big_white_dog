	

function volumeOfSphere(){
	let volume = 0;
	let radius = document.getElementById("radius").value;
	// for (let i = 0; i=2; i++ ){
	// 	let radiusHigh = radius[i];
	let volume = 4/3 * Math.PI * Math.pow(radius, 3);
	document.getElementById("volume").value;

	return volume

}
let volume = volumeOfSphere()
console.log(volume)
