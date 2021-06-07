// function6 - Find Average
var array = [25,50,75,100];
var counter = 0;
var sum = 0;
var average = 0;
function findAverage(){
    for (var counter = 0; counter != (array.length); counter++){
        sum = sum + array[counter];
    }
    average = sum/array.length;
    return average;
}
console.log(findAverage());