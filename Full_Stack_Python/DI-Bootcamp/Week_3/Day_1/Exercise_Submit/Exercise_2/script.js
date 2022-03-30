

let documentElement = document.body

let ulElementFirst = document.body.children[1];
console.log(ulElementFirst)

let ulElementSecond = document.body.children[2];
console.log(ulElementSecond)

let ulLiRichard = ulElementFirst.children[1]
console.log(ulLiRichard)

ulLiRichard.textContent = "Richard"



// This is one way to do it although here i did repeat my self

let allLis = document.querySelectorAll("ul li");
console.log(allLis);

console.log(allLis[0])


allLis[0].textContent = "Matan"
allLis[2].textContent = "Matan"




// let ulElementQuery = document.querySelectorAll("ul > li");
// console.log(ulElementQuery);

// let firstLis = 

// ulElementQuery[3].innerHTML = "dfsgdsfgdsfg"



// let liElementList1 = ulElementQuery[0];
// console.log(liElementList1)




// let liElementList1 = ulElementFirst.firstElementChild;
// console.log(liElementList1)


// let liElementList2 = ulElementSecond.firstElementChild;
// console.log(liElementList2)


let newEndLiOne = document.createElement("li");
let newEndLiOneText = document.createTextNode("Hello Students");

newEndLiOne.appendChild(newEndLiOneText);
ulElementFirst.appendChild(newEndLiOne);

let newEndLiTwo = document.createElement("li");
let newEndLiTwoText = document.createTextNode("Hello Students");

newEndLiTwo.appendChild(newEndLiTwoText);
ulElementSecond.appendChild(newEndLiTwo);


//----------------------------------------------------------------

let sarahLi = allLis[3]
console.log(sarahLi);

sarahLi.remove();


