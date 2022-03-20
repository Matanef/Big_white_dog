//Part 1

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];


let myWatchedSeriesLength = myWatchedSeries.length
console.log(`myWatchedSeriesLength=` ,myWatchedSeriesLength);


let myWatchedSeriesSentence = myWatchedSeries.toString();
console.log('myWatchedSeriesSentence=', myWatchedSeriesSentence);


let str = ` I Watched ${myWatchedSeriesLength} series ${myWatchedSeriesSentence}`
console.log(str);

//Part 2
myWatchedSeries.splice(2, 1, "Friends");
console.log(myWatchedSeries);

myWatchedSeries.push("Bojack");
console.log(myWatchedSeries);

myWatchedSeries.unshift("can't think of one right now");
console.log(myWatchedSeries);

myWatchedSeries.splice(1, 1);
console.log(myWatchedSeries);

console.log(myWatchedSeries);





