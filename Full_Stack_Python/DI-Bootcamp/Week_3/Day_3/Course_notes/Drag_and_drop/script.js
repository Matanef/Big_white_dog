//1. Retrieve the div
let boxToDrag = document.getElementById("item");

// 2. I add the event listener of dragstart to the box
boxToDrag.addEventListener("dragstart", startDraggingTheItem);

// 3. The function startDraggingTheItem is called when we start dragging an item
function startDraggingTheItem (event) {
	console.log(event);
	// 3.2 - we replace the class of the item
	boxToDrag.classList.replace("draggedItem","startDragging");
	// 3.3 - setData takes 2 argument - the type of the data, 
	// and the id of the element we want to drag
	// dataTransfer.setData, sets the data we want to drop in the future
	event.dataTransfer.setData("text/plain", event.target.id);
}

// 4. Retrieve the valid drop zones
let dropZones = document.getElementsByClassName("dropzone");

// 5. Create a function named addEventToDropZone
// that loops through the dropzones from the HTML
// and add to each of them several events
function addEventToDropZone (){
	for (let zone of dropZones) {
		zone.addEventListener("dragover", draggingOverDropZone);
		zone.addEventListener("drop", droppingOnDropZone)
	}
}

addEventToDropZone ()

// 6. This function is called when we drag over an element
// we prevent the default action and change the style
function draggingOverDropZone (event) {
	event.preventDefault();
	event.target.classList.replace("zone", "dragover");
}

// 7. This function is called when we drop an element
// we prevent the default action
function droppingOnDropZone (event){
	event.preventDefault();
	// 7.1 - we get the data we set (from dragstart event) 
	// so we retrieve the id of the element we drag
	let idOfbox = event.dataTransfer.getData("text/plain");
	// we retrieve the div with this id and append it in the drop zone
	let divToDrop = document.getElementById(idOfbox);
	event.target.appendChild(divToDrop);
}