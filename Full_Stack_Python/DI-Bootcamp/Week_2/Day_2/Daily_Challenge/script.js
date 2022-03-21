let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not")
console.log(wordNot)
let wordBad = sentence.indexOf("bad")
console.log(wordBad)

let arr = sentence.split(` `)
console.log(arr)


let result = sentence.replace(`not that bad`, "good");
console.log(`${result.toUpperCase()}, this is just a practice and an example for my self`);

if (wordNot<wordBad){
	console.log(result)
} else if (wordNot<wordBad){
	console.log(sentence)
}else if (wordNot=-1, wordBad=-1){
	console.log("The movie is not that bad, I like it")
}




// if (sentence.indexOf(wordNot) && sentence.indexOf(wordBad)) {
// 	console.log(result)
// }


// if (sentence.indexOf(wordNot) && sentence.indexOf(wordBad)) {
// 	console.log("The movie is good, I like it")
// } else if(false) {
// 	console.log(sentence)
// }

// let arr = sentence.split(``)
// console.log(arr)