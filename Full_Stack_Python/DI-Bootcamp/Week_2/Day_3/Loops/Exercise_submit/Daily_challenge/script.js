let astrixlength = 6;
//we have 6 lines that needs to be crated, hence we will already define
//the row length/
let astrix = '';
// no spaces
for (let i = 1; i<=astrixlength; i++){
	astrix +="*";
	console.log(astrix);
}

let astrixLength = 6;
let astrixs='rrrr';
for (let i = 1; i <= astrixlength; i++){
	for (let j = 1; j <= i; j++){
		astrixs +="*";
	}
	console.log(astrixs);
	astrixs = '';
}