/*Задача №3. Напишите программу, которая будет выдавать название дня недели по заданному номеру.
3 -> Среда 
5 -> Пятница
*/

Console.WriteLine("Введите день недели");
string number1Str = Console.ReadLine();
int number1 = Convert.ToInt32(number1Str);

if(number1 == 1)
{
Console.WriteLine("пн");
} else if (number1 == 2){
    Console.WriteLine("вт");
}

else if (number1 == 3){
    Console.WriteLine("ср");
}
else if (number1 == 4){
    Console.WriteLine("чт");
}
else if (number1 == 5){
    Console.WriteLine("пт");
}
else if (number1 == 6){
    Console.WriteLine("сб");
}
else if (number1 == 7){
    Console.WriteLine("вс");
} else
    Console.WriteLine("ввели не число недели (1-7)");
