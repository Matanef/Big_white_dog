let tableElement = document.getElementById("sampleTable");
console.log(tableElement);

let trElement = document.getElementsByTagName('tr')

let tdElement = document.getElementsByTagName('td')
console.log(tdElement);

function insertRow (){
	let tr = document.createElement('tr');
	let rowNum = document.getElementsByTagName("tr").length
	// let cellNum = 
	let cellText = document.createTextNode
	let tableFunc = document.getElementById("sampleTable");
	let trFunc = document.getElementsByTagName('tr');
	let tdElement = document.getElementsByTagName('td')
	let tdText = document.createTextNode(`Row ${tdElement.length} cell1`)
}
};