let wordListArr = []

for (let i = 1; i <= 4; i++){
    wordListArr.push(prompt(`Please enter the ${i}# word`))
}

console.log(wordListArr)
let wordStr =  wordListArr.join(", ");
console.log(wordStr); 
let brk = wordStr.split(` `);
let res = brk.join(" ")
console.log(res);

let longestWord = 0
for (let l = 0; l <brk.length; l++){
    for (let nest =0; nest <=l; nest++ )
        if(nest.length > longestWord){
            longestWord = brk[l].length;
            console.log(wordListArr[l] + "*");
        }
    }
    console.log(longestWord)





