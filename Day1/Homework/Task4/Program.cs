/*Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

2, 3, 7 -> 7
44 5 78 -> 78
22 3 9 -> 22*/

Console.WriteLine("Введите число #1:");
string numberFirstStr = Console.ReadLine();
int numberFirst = Convert.ToInt32(numberFirstStr);

Console.WriteLine("Введите число #2:");
string numberSecondStr = Console.ReadLine();
int numberSecond = Convert.ToInt32(numberSecondStr);

Console.WriteLine("Введите число #3:");
string numberThirdStr = Console.ReadLine();
int numberThird = Convert.ToInt32(numberThirdStr);

int max = numberFirst;

if(numberFirst > max) max = numberFirst;
if(numberSecond > max) max = numberSecond;
if(numberThird > max) max = numberThird;

Console.WriteLine($"Больше всех - {max}!");