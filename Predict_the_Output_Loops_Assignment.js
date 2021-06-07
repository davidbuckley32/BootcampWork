// Predict 1
for(var num = 0; num < 15; num++){
    console.log(num)
}

// console will log 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
// console will not log 15, since the condition is evaluated as false
// the loop will stop

// Predict 2
for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}

// console will log 3, 9
// i starts at 1 and will increase by 2 until it reaches 11
// since 11 is not less than 10, the loop will stop

// Predict 3
for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}

// console will log 1, 4, 5, 8, 10, 11, 14, 16
// the loop will stop when it reads j as equaling 16