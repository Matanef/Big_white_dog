let solarArray = [
{name: 'Mercury', moons: 0, color: "lightgrey"},
{name: 'Venus', moons: 0, color: "lightgrey"},
{name: 'Earth', moons: 1, color: "blue"},
{name: 'Mars', moons: 2, color: "#c94c4c"},
{name: 'Jupiter', moons: 79, color: "#bc5a45"},
{name: 'Saturn', moons: 82, color: "#dac292"},
{name: 'Uranus', moons: 27, color: "lightblue"},
{name: 'Neptun', moons: 14, color: "darkblue"},
{name: 'Pluto', moons: 5, color: "lightgrey"}
]

let planetSection = document.querySelector('section');
console.log(planetSection);
for (let planet of solarArray){
    let planetDivs = document.createElement('div')
    planetDivs.classList.add('planet');
    planetDivs.innerText = planet.name;
    planetDivs.style.backgroundColor = planet.color
    planetSection.appendChild(planetDivs);
    console.log(planetDivs);
}

