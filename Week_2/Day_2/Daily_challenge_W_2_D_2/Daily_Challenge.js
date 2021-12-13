let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.indexOf("not")
let wordBad = sentence.indexOf("bad")


let result = sentence.replace(`not that bad`, "good");
console.log(result.toUpperCase());


if (sentence.indexOf(wordNot) && sentence.indexOf(wordBad)) {
	console.log(result)
}


if (sentence.indexOf(wordNot) && sentence.indexOf(wordBad)) {
	console.log("The movie is good, I like it")
} else if(false) {
	console.log("The movie is not that bad, I like it")
}