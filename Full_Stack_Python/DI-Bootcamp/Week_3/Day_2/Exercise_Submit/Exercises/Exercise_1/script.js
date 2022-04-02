
let h1 = document.querySelectorAll("h1")[0];
console.log(h1)

let para = document.querySelector("article")
para.removeChild(para.lastElementChild)  

let h2 = document.querySelector("h2")
h2.onclick = function() {
	h2.style.background = 'red'
}
let h3 = document.querySelector("h3")
h3.addEventListener("click" ,display)
function display() {
	h3.style.display = "none"
}
let bold = document.querySelector("button")
bold.addEventListener('click', makebold)
function makebold() {
	para.style.fontWeight = 'bold'
}
h1.addEventListener("mouseover", hover)
function hover() {
	h1.style.fontSize = Math.random()*300 + "px" 
}
let p2 = para.children[4]
p2.onmouseover = function() {
	p2.style.transition = "opacity 3s"
	p2.style.opacity = "0"
}