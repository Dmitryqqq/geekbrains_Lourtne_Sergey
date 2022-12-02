/* Задача 28: Напишите программу, которая принимает на вход число N и выдаёт произведение чисел от 1 до N.
4 -> 24 
5 -> 120
*/

//получение числа с консоли
int GetNumber(string message)
{
    bool isCorrect = false;
    int result = 0;

    while(!isCorrect)
    {
        Console.WriteLine(message);
        if(int.TryParse(Console.ReadLine(), out result))
        {
            isCorrect = true;
        }
        else
        {
            Console.WriteLine("Ввели не число");
        }
    }
    
    return result;
}

int num = GetNumber("Введите число");
int result = 1;

for (int i = 1; i <= num; i++)
{
    result = result * i;
}

Console.WriteLine($"Произведения от 1 до {num} равно {result}");
