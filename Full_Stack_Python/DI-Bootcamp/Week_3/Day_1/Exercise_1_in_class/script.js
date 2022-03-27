
let documentElement = document.body
console.log(documentElement)
let divElement = document.body.children[0];
console.log(divElement)
let divElementSecond = document.body.firstElementChild;
console.log(divElementSecond)


let ulElement = documentElement.children[1];
console.log(ulElement)
let ulElementSecond = documentElement.nextElementSibiling;
console.log(ulElementSecond)

let liElement = document.body.children[1]
console.log(liElement)
let liElementSecond = ulElement[0];
console.log(liElementSecond)


const lieElementSecond = document.getElementsByTagName('li');

for (i = 0; i < liElementSecond.length; i++) {
	liElementSecond[i].style.border = '1px solid blue';
}

// let divElementFirstWay = document.body.children[0];
// console.log(divElementFirstWay)
// let divElementSecondWay =  document.body.firstElementChild;
// console.log(divElementSecondWay)

// let ulElementFirstWay = document.body.children[1];
// console.log(ulElementFirstWay)
// let ulElementSecondWay = divElementFirstWay.nextElementSibling;
// console.log(ulElementSecondWay)

// let liPeteFirstWay = ulElementFirstWay.lastElementChild;
// console.log(liPeteFirstWay)
// let liPeteSecondWay = ulElementFirstWay.children[1];
// console.log(liPeteSecondWay)