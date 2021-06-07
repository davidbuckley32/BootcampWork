// function8 - Greater Than Y
var y = 32;
var i = 0;
var array = [1, 4, 77, 103, 999999999];
var greater = [];
function greaterThanY(){
    for (i = 0; i != array.length; i++){
        if (array[i] > y){
            greater.push(array[i]);
        }
    }
    return greater;
}
console.log(greaterThanY());