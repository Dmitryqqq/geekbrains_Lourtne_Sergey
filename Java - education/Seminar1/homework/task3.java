import java.util.Scanner;

public class task3 {
    public static void main(String[] args) {
        System.out.print("Введите число: ");
        Scanner n1 = new Scanner(System.in);
        int number1 = n1.nextInt();

        System.out.print("\nВыберите операцию (+, -, /, *): ");
        Scanner in = new Scanner(System.in);
        String znak = in.nextLine();

        System.out.print("\nВведите число: \n");
        Scanner n2 = new Scanner(System.in);
        int number2 = n2.nextInt();

        switch (znak) {
            case  ("+"):
                System.out.print(("Ответ: " + (number1 + number2)));
                break;
            case  ("-"):
                System.out.print(("Ответ: " + (number1 - number2)));
                break;
            case  ("/"):
                System.out.print(("Ответ: " + (number1 / number2)));
                break;
            case  ("*"):
                System.out.print(("Ответ: " + (number1 * number2)));
                break;
            default:
                System.out.print("Доступны только операции +, -, / или *!");
                break;
        }
}
}