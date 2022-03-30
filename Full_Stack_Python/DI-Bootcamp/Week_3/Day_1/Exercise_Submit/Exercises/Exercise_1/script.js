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

console.log(ulElement)

let newLi1 = document.createElement("li");
let textNode1 = document.createTextNode("Logout");

newLi1.appendChild(textNode1)
ulElement.appendChild(newLi1);

let firstElementInList = ulElement.firstElementChild
console.log(firstElementInList)
let text1 = firstElementInList.textContent;
console.log(text1);



let lastElementInList = ulElement.lastElementChild
console.log(lastElementInList);
let text2 = lastElementInList.textContent;
console.log(text2);







