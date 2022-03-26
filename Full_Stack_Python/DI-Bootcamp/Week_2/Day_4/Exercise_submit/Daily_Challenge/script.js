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

// let max = parseInt(Math.max(wordStr));
// console.log(max) 

// function longWord(){
//     let longestWord = 0
//     for (let l = 0; l <brk.length; l++){
//         let currentWord = brk[l];
//         let longWord = currentWord.length;
//         if(longWord > currentWord){
//             let longestWord = longWord;
//             // console.log("*" +brk[l]+ "*");
//             console.log(longestWord)
//         }
//     }
//     return longestWord
// }


// function longWord(){
    function massiveWord(wordListArr) {
        let longestWord = 0
        for (let l = 0; l <brk.length; l++){
            if(brk.length > longestWord){
                longestWord = brk.length;
                // console.log(longestWord);
            }
        }
        return longestWord
    }
    massiveWord();



    function frameWords (wordListArr){
        let longestWord = massiveWord(wordListArr)
        let sign = "*";

        let frame = sign.repeat(longestWord + 4)
        console.log(`${frame}`)
        for (let j = 0; j < wordListArr; j++){
            let empty = " ";
            let currWord = wordListArr[j]
            let space = longestWord - currWord.length;
            console.log(`* ${currWord} ${empty.repeat(space)}*`);
        }
    }

    frameWords();

// longWord(longestWord);


// function frameWord (){
//     let longestWord = 
// }