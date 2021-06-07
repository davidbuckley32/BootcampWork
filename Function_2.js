// function2  - Get Even 1000 
var sum = 0;
var num = 2;
function getEven1000() {
    for (var num = 2; num < 1001; num+=2) {
        sum = sum + num;
    }
    return sum;
}
console.log(getEven1000());