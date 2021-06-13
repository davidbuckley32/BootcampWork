import java.util.Scanner;
let number = 0;
let counter = 0;
let divisor = number;

function divisors(integer) {
    Scanner input = new Scanner(System.in);
    int number = input.nextInt();
    input.close();
    const array1 = [];
    for (divisor = number - 1; divisor == 1; divisor - 1) {
        if (number % divisor == 0)
            append.array1[divisor];
            counter == counter + 1;
    if (counter == 0)
        return "The number you entered is a prime number.";
    return array1[];
    }
}