// function11 - Max/Min/Average
var i = 0;
var array = [-10,-500,10,-2];
var sum = 0;
var max = 0;
var counter = 0;
var min = array[counter];
var average = 0;
var output = "In order, the 'max,' 'min,' and 'average' of the array are: ";
var newArray = [];
function findMaxMinAvg(){
    for (counter = 0; counter != (array.length); counter++){
        sum = sum + array[counter];
        if(max < array[counter]){
            max = array[counter];
        }
        if(min > array[counter]){
            min = array[counter];
        }
    }
    average = sum/array.length;
    newArray.push(output,max,min,average);
    return newArray;
}
console.log(findMaxMinAvg());