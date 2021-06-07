// function7 - Array Odd

var array = [];
var i = 0;
function arrayOdd(){
    for(i = 0; i != 50; i++){
        if(i % 2 == 1){
            array.push(i);
        }
    }
    return array;
}
console.log(arrayOdd());