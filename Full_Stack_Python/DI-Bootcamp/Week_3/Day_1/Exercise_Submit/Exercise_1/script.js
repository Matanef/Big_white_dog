let documentElement = document.body

let divElement = document.body.children[0];
console.log(divElement)
divElement.setAttribute("id", "socialNetworkNavigation");


let ulElement = divElement.lastElementChild
console.log(ulElement)

let newLi = document.createElement("li");
let textNode = document.createTextNode("something something dark side");

newLi.appendChild(textNode)
ulElement.appendChild(newLi);

let ulElement = divElement.lastElementChild
console.log(ulElement)

let newLi1 = document.createElement("li");
let textNode1 = document.createTextNode("Logout");

newLi1.appendChild(textNode1)
ulElement.appendChild(newLi1);








