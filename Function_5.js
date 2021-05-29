// function5 - Find Max
    var array = [-3,3,-8,-7];
    var counter = 0;
    var max = array[counter];
    function findArrayMax(){
        for (var counter = 0; counter != array.length; counter++){
            if(array[counter] >= max){
                max = array[counter];
            }
        }
        return max;
    }
    console.log(findArrayMax());