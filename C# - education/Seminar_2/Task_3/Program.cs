// Напишите программу, которая будет принимать на вход два числа и выводить, является ли второе число кратным первому. 
//Если число 2 не кратно числу 1, то программа выводит остаток от деления.
// 34, 5 -> не кратно, остаток 4 
// 16, 4 -> кратно

Console.WriteLine("Введите число #1:");
string numberFirst = Console.ReadLine();
int number1 = Convert.ToInt32(numberFirst);

Console.WriteLine("Введите число #2:");
string numberSecond = Console.ReadLine();
int number2 = Convert.ToInt32(numberSecond);

int result = number1 % number2;

if(result == 0) {
    Console.WriteLine($"{number1} кратно {number2}!");
} else {
    Console.WriteLine($"Остаток {result}.");
}