// function10 - Negatives
var i = 0;
var array = [1,5,10,-2];
function negative(){
    for (i = 0; i != array.length; i++){
        if(array[i] < 0){
            array[i] = 0;
        }
    }
    return array;
}
console.log(negative());