let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let arr = []

for (var i =0; i < names.length; i++){
	console.log(names[i])
	let name = names[i];
	console.log(names[0]);
	arr.push(name[0]);
}

console.log(arr.sort().join(``));


console.log("-------------------------")

let societyName = "";
names = names.sort();
console.log(names);

for (let person of names){
	console.log(`The first letter of the name ${person} is ${person.charAt(0)} `)

	societyName += person.charAt(0);
}
console.log(`The Society Name is ${societyName}`);