// function 1 - Get 1 to 255
var array = [];
function oneTo255(test) {
    for(var num = 1; num< 256; num++) {
        array.push(num);
    }
    return array;
    }
console.log(oneTo255());