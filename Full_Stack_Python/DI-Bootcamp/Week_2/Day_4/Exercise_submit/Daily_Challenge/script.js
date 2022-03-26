let text = prompt("please enter a sentence")
let text_arr = text.split(" ");
console.log(text_arr);

let longest = get_longest(text_arr);
let border = new Array(longest + 8).join("*")


console.log(border)
for (word of text_arr){
	console.log("* " + word + new Array(longest - word.length +4).join(" ") + " *");
}
console.log(border)

function get_longest(arr){
	let longest = 0;

	for (word of arr){
		if (word.length > longest){
			longest = word.length
		}
	}
	return longest;
}