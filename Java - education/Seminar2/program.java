import java.util.Scanner;
// Дано четное число N (>0) и символы c1 и c2. Написать метод, который 
// вернет строку длины N, которая состоит из чередующихся символов c1 и c2, начиная с c1.

// 6 a b
// Вернуть: ababab

// public class program {
//     public static void main(String[] args) {
//         System.out.print("Введите число: ");
//         Scanner in = new Scanner(System.in);
//         int n = in.nextInt();
    
//         System.out.print("Введите символ: ");
//         char s1 = in.next().charAt(0);
        
//         System.out.print("Введите символ: ");
//         char s2 = in.next().charAt(0);

//         System.out.print(twoChar(n, s1, s2));

//         in.close();
//     }

//     public static String twoChar(int n, char s1, char s2) {
//         StringBuilder result = new StringBuilder();

//         for (int i = 0; i < n / 2; i++) {
//             result.append(s1).append(s2);
//         }

//         return result.toString();
//     }
// }

// 2) Напишите метод, который сжимает строку. Пример: вход aaaabbbcddaaa.
//  результат - a4b3cd2a3
// .charAt(i)
// stroka = "Привет"

// stroka1 = new String

// stroka1 = "Привет"

// stroka == stroka1   ----> False

// stroka.equals(stroka1) ------> True

// public class program {
//     public static void main(String[] args) {
//         System.out.print("Введите строку: ");
//         Scanner in = new Scanner(System.in);
//         String str = in.nextLine();

//         System.out.print(zipStroki(str));

//         in.close();
//     }

//     public static String zipStroki(String str) {
//         StringBuilder result = new StringBuilder();
//         int count = 1;

//         for (int i = 0; i < str.length() - 1; i++) {
//             if (str.charAt(i) == str.charAt(i+1)) {
//                 count += 1;
//             } else {
//                 result.append(str.charAt(i));

//                 if (count > 1) {
//                     result.append(count);
//                 }

//                 count = 1;
//             }
//         }

//         result.append(str.charAt(str.length() - 1));

//                 if (count > 1) {
//                     result.append(count);
//                 }

//         return result.toString();
//     }
// }

import java.io.File;
import java.io.FileWriter;
// задание: записать слово TEST в файл 10 раз
public class program {
    public static void main(String[] args) {
        Integer n = 10;
        String text = "TEST";
        String file_name = "1.txt";
        File file = new File(file_name);
        try{
            FileWriter writer = new FileWriter(file,false);
            for (int i = 0; i < n; i++){
                writer.write(text);
                writer.write("\n");
            }
            writer.close();
            System.out.println("Получилось!)");
        }
        catch (Exception e){
            System.out.println("Что то пошло не так");
        }
    }
}