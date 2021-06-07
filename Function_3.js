//function 3 - Some Odd 5000
var sum = 0;
var num = 1;
function sumOdd5000() {
    for (var num = 1; num < 5001; num+=2) {
        sum = sum + num;
    }
    return sum;
}
console.log(sumOdd5000());