let bodyElement = document.body
console.log(bodyElement)

let articleelement = bodyElement.children[0]
console.log(articleelement)

let headerFirst = articleelement. children[0]
console.log(headerFirst)

// let hOneElement = document.getElementsByTagName("h1");
// console.log(hOneElement);
// let textHeader = firstElementInList.textContent
// console.log(textHeader)

let parasElements  = document.querySelectorAll('article > p')
console.log(parasElements)

console.log(parasElements[0])


for (let i = 0; i <= parasElements.length; i++){
	if (i == parasElements.length)
		// let lastpar = 
	console.log(i)
}
console.log(parasElements.length)