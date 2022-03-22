let family = {
	members : {
		Father : "Raphael" ,
		Mother : "Shirly",
		Son : "Matan",
		Daughter : "Dana",
		Dog : "Lanou",
	}
};
// console.log(family)
console.log("----------------")

for (let x in family[`members`]){
	console.log(x);
}
console.log("----------------")

for (let [x, value] of Object.entries(family.members))
	console.log(`${value}`)

console.log("----------------")

// Object.values(family.members).forEach(val => console.log(val));


// for (let y in family){
// 	console.log(y);
// }
// for (let values = 0; values > family[members].length, values++)
// 	console.log(values);



// 	let y = family.m[1];
// console.log(y);