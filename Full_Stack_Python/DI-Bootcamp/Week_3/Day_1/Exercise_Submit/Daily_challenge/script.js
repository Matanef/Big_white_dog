let solarArray = [
{name: 'Mercury', moons: 0, color: "#c8c3cc"},
{name: 'Venus', moons: 0, color: "#ff7b25"},
{name: 'Earth', moons: 1, color: "blue"},
{name: 'Mars', moons: 2, color: "#c94c4c"},
{name: 'Jupiter', moons: 79, color: "#bc5a45"},
{name: 'Saturn', moons: 82, color: "#dac292"},
{name: 'Uranus', moons: 27, color: "#b7d7e8"},
{name: 'Neptun', moons: 14, color: "#034f84"},
{name: 'Pluto', moons: 5, color: "#cab577"}
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
    for (let moon of solarArray){
        let moonDivs  = document.createElement('div');
        moonDivs.classList.add('moon');
        moonDivs.innerText = planet.moons;
        moonDivs.style.backgroundColor = planet.color
        planetDivs.appendChild(moonDivs);
    }
}

