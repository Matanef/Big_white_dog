let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let arr = []

for (var i =0; i < names.length; i++){
	console.log(names[i])
	let name = names[i];
	console.log(names[0]);
	arr.push(name[0]);
}

console.log(arr.sort().join(``));
