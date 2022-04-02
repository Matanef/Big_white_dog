let form = document.forms[0]
console.log(form)
let firstIndex = form.elements.fname
for (let a = 0; a<form.elements.length;a++){
    let c = form.elements[a]      
    console.log(c)
}
for (let a = 0; a<form.length;a++){
    let f = form.elements[a].name      
    console.log(f)
}
form.addEventListener("submit",function101)
function function101(e){
    e.preventDefault()
    let inputValue1 = form.elements[0].value
    let inputValue2 = form.elements[1].value
    if (inputValue1&&inputValue2){
        // let li = document.createElement("li")
        // let textNode = document.createTextNode(`${inputValue1} ${inputValue2}`)
        // li.append(textNode)
        // let ul = document.querySelector("ul")
        // ul.append(li)
        for (let a = 0;a<e.target.elements.length-1;a++){
            let currentInput = e.target.elements[a];
            let li = document.createElement("li")
            let textNode = document.createTextNode(currentInput.value)
            li.append(textNode)
            let ul = document.querySelector("ul")
            ul.append(li)
        }
    }}