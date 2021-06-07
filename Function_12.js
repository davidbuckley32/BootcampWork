// function12 - Swap Values
var array = [-10,2,5,1];
var oldAlpha = array[0]
var oldOmega = array[array.length - 1];
var Omega = oldAlpha;
var Alpha = oldOmega;
function swapTime(){
    array[0] = Alpha;
    array[array.length - 1] = Omega;
    return array;
}
console.log(swapTime());
