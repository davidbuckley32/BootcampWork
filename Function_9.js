// function9 - Squares
var i = 0;
var array = [1,5,10,-2];
function squareLicious(){
    for (i = 0; i != array.length; i++){
        array[i] = array[i] * array[i];
    }
    return array;
}
console.log(squareLicious());