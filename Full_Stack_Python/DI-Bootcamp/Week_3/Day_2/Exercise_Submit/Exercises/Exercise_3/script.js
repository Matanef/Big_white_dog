let boldItems = document.getElementsByTagName("strong");

function getBoldItems(){

	return boldItems;
}
console.log(getBoldItems())

function highlight(){
	let boldItemFromParagraph = getBoldItems();
	for (let i = 0; i < boldItemFromParagraph.length ; i++){


		boldItemFromParagraph[i].style.color = "blue";

	}
	console.log(boldItemFromParagraph)
}

function returnNormal(){
	let boldItemFromParagraph = getBoldItems();
	for (let i = 0; i < boldItemFromParagraph.length ; i++){
		boldItemFromParagraph[i].style.color = "black";

	}
	console.log(boldItemFromParagraph)
}


let p = document.querySelector("#paragraph");
p.addEventListener("mouseover", highlight)
p.addEventListener("mouseout", returnNormal)

