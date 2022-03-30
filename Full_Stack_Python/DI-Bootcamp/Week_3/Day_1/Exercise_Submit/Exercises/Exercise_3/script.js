// 1. locating the element
let divElement = document.querySelector("div")
divElement.style.backgroundColor = "lightblue"
divElement.style.padding = "15px"

let johnLi = document.querySelector("ul").firstElementChild;
johnLi.style.visibility = "hidden";

let peteLi = document.querySelector("ul").lastElementChild;
peteLi.style.border = "dotted pink 3px"


let bodyElement = document.body
bodyElement.style.fontSize = "48px"

let johnText = johnLi.innerHTML
console.log(johnText)

let peteText = peteLi.innerText
console.log(peteText)

if (divElement.style.backgroundColor == "lightblue"){
	alert(`Chello, this is appearing because the div backgroundColor is lightblue, in addition ${peteText} and ${johnText}`);
};

