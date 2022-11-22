/*Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

a = 5; b = 7 -> max = 7
a = 2 b = 10 -> max = 10
a = -9 b = -3 -> max = -3*/

Console.WriteLine("Введите число #1:");
string numberFirstStr = Console.ReadLine();
int numberFirst = Convert.ToInt32(numberFirstStr);

Console.WriteLine("Введите число #2:");
string numberSecondStr = Console.ReadLine();
int numberSecond = Convert.ToInt32(numberSecondStr);

if(numberFirst > numberSecond)
{
Console.WriteLine($"Max = {numberFirst}, min = {numberSecond}");
} else if(numberFirst < numberSecond) {
    Console.WriteLine(($"Max = {numberSecond}, min = {numberFirst}"));
} else {
    Console.WriteLine("Числа равны!");
    }