let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}


// let shoppingList = ["banana", "orange", "apple"];

// for (let i = 0; i = 0; i++){
//     console.log("i is : ", i)
//     console.log("in stock : ", stock[i])
//     console.log(`length of ${stock[i]} is : ${stock[i].length}`)
//     for (let j = 0; j < stock[i].length; j++){
//         console.log("j is : ", j)
//         console.log(`the ${j+1}# letter of ${stock[i]} is ${stock[i][j]}`)
//     }
// }




let shoppingList = ["banana", "orange", "apple"];
for (element of shoppingList) {
    let appleP = prices["apple"]
        console.log(shoppingList + " not in stock")
} 




// function findTotalSum () {
//     let sum = 0;
//     for (let price in shoppingList) {
//         sum = sum + price;
//     }
//     return sum;
// }
// console.log(findTotalSum());