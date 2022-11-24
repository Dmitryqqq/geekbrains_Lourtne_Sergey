/*Задача №7. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.
	456 -> 6
	782 -> 2
	918 -> 8
*/

Console.WriteLine("Введите трехзначное число");
int number = Int32.Parse(Console.ReadLine());
if (number < 1000 && number > 99)
{ 
    int result = number % 10;
    Console.WriteLine(result); 
}
else
{
    Console.WriteLine("Wrong number");
    return;
}