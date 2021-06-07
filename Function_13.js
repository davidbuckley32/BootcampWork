//function13 - Number to String
var array = [-1,-3,2];
var string = "Dojo";
var counter = 0;
function numberToString(){
    for(string = "Dojo"; counter != array.length; counter++){
        if(array[counter] < 0){
            array[counter] = string;
        }
    }
    return array;
}
console.log(numberToString());