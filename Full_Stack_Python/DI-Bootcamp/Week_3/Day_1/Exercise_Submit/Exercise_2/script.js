

let documentElement = document.body

let ulElementFirst = document.body.children[1];
console.log(ulElementFirst)

let ulElementSecond = document.body.children[2];
console.log(ulElementSecond)

// let ulElementAll = ulElementFirst || ulElementSecond
// console.log(ulElementAll)


// let ulElementByTag = document.getElementsByTagName(`ul`).firstElementChild
// console.log(ulElementByTag)

let liElement = ulElementFirst.lastElementChild
console.log(liElement);

let liElementFirst = ulElementFirst.firstElementChild
console.log(liElementFirst);


let liPeteFirstWay = ulElementFirst.firstElementChild;
console.log(liPeteFirstWay)

// for (let i = 0; i=1)

liElement.innerHTML = "Richard";


let liElementFirstItem = document.getElementsByClassName("first");
console.log(liElementFirstItem);

liElementFirstItem.outerHTML = "Matan";



// let firstLi = ulElementByTag.children[0];
// console.log(firstLi)





// let containerQuerySelector = document.querySelector("#first")
// console.log(containerQuerySelector)


// containerQuerySelector.innerHTML = "Matan"


// for (i = 0; i <=1; i++) {
// 	liElementSecond[i].style.border = '1px solid pink';
// }
// ulElementByTag.innerHTML = `Matan`;






// let ulElementByTag = document.getElementsByTagName(`ul`);
// let liElementSecond = ulElementByTag.firstElementChild;
// for (let i = 0; i <=1; i++) {
// 	for(let j=0; j<1; j++){
// 		ulElementByTag[i].style.border = '1px solid blue';
// 		liElementSecond[j].innerHTML = "Matan"
// 		console.log(liElementSecond )
// 	}
// }

