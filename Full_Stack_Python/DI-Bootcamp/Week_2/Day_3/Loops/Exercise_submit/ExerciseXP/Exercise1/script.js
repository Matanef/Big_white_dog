let people = ["Greg", "Mary", "Devon", "James"];
let peopleLess = people.shift();
console.log(peopleLess);
console.log(people);

people.splice(2, 1, "Jason");
console.log(people);

people.push("Matan");
console.log(people);

console.log(people.indexOf("Mary"));

let peopleCopy = people.slice(1);
console.log(peopleCopy)

console.log(people.indexOf("Foo"));
//returns -1 since it is not part of the array


let last = people[people.length -1];
console.log(last);


// for (let i = 0; i = people.length -1; i++);
// 	console.log(people[i]);

// for (let elements of people){
// 	console.log(elements);

// }
let jasonind = people.indexOf("Jason")
console.log(jasonind)

console.log(people)
console.log("|")
for (let i = 0; i< jasonind; i++){
	console.log(people[i])
}








