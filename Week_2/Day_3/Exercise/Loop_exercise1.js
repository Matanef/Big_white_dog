let people = ["Greg", "Mary", "Devon", "James"]
console.log(people)

let gregword = people.indexOf("Greg")
people.splice(gregword, 1)
console.log(people); 

let elemJames = people.indexOf("James");

if (elemJames) {
let remove = elemJames;
people.splice(elemJames, remove, "Jason");
console.log(people)
}

people.push("Matan")
console.log(people);


console.log(people.slice(1,-1));


console.log(people.indexOf("Foo"))
// the result is a -1 since the word "FOO" does not appear in
// our array "people".

let last = people.slice(-1)
console.log(last)

for (let elements of people){
  console.log(elements);

}

for (let elements of people){
  console.log(elements);
  if (elements == "Jason"){
  	break
  }
}

//with the help of .length i follow the change of the 
//amount of elements in an array, even if there will 
//be any future change the code we will write based 
//on that should be updated
