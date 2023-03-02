import java.util.Arrays;
import java.util.Scanner;

// Написать программу, которая запросит пользователя ввести <Имя> в консоли. 
// Получит введенную строку и выведет в консоль сообщение “Привет, <Имя>!”
// import java.util.Scanner;

// import java.util.Scanner;

// public class Task_1 {
//     public static void main(String[] args) {
//         System.out.print("Ваше имя: ");
//         Scanner in = new Scanner(System.in, "Cp866");
//         String name = in.nextLine();
//         System.out.println("Привет, " + name + "!");
//     }
// }

// Дан массив двоичных чисел, например [1,1,0,1,1,1,1,0,1,1,1],
// вывести максимальное количество подряд идущих 1.

// Вывод: 4



// public class program {
//     public static void main(String[] args) {
//         int[] arr = new int[] {1,1,0,1,1,1,1,0,1,1,1,1,1,1};
//         int count = 0;
//         int total = 0;

//         for (int i = 0; i < arr.length; i++) {
//             if (arr[i] == 1) {
//                 count++;
//             }
//             else {
//                 if (count > total) {
//                     total = count;
//                 }
//                 count = 0;
//             }
//         }
    
//         System.out.println(Arrays.toString(arr));

//         if (total > count) {
//             System.out.println(total);
//         } else {
//             System.out.println(count);
//         }

//     }
// }

// Дан массив nums = [3,2,2,3,4,3] и число val  вводим с клавиатуры 

// Если в массиве есть числа, равные заданному, нужно перенести 
// эти элементы в конец массива. 
// Таким образом, первые несколько (или все) элементов массива 
// должны быть отличны от заданного, а остальные - равны ему.
// Ввод: 3
// Вывод:
// 2, 2, 4, 3, 3, 3

public class program{
    public static void main(String[] args) {
        int[] arr = new int[] {3, 2, 3, 6, 4, 3}; 
        int[] mas = new int[arr.length];
        int left = 0;
        int rith = arr.length - 1;

        Scanner n = new Scanner(System.in);
        System.out.print("Введите число: ");
        int nam = n.nextInt();
        n.close();

        System.out.println(Arrays.toString(arr));
        // System.out.println(Arrays.toString(mas));
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == nam) {
                mas[rith] = arr[i];
                rith --;
            }
            else {
                mas[left] = arr[i];
                left ++;
            }
        }
        System.out.println(Arrays.toString(mas));
    }}

