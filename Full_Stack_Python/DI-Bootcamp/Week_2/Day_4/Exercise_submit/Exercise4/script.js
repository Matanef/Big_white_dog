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

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0
    for (let fruList of shoppingList){
        // console.log(stock[fruList]);
        if (stock[fruList] >0){
            total += prices[fruList]
            stock[fruList]= stock[fruList] - 1
        }

    }
    console.log(stock);
    return total;

}


myBill();

let a = myBill()
console.log(a);


console.log


