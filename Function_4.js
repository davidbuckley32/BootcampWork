// function4 () {
    var array = [1,2,3,4,5];
    var sum = 0;
    function findArraySum(){
        for (var counter = 0; counter != array.length; counter++){
            sum = array[counter] + sum;
        }
        return sum;
    }
    console.log(findArraySum());