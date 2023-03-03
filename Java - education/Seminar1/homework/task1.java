import java.util.Scanner;

public class task1 {
        public static void main(String[] args) {
                System.out.print("Введите число: ");
                Scanner n = new Scanner(System.in);
                int nam = n.nextInt();
                int countSum = 0;
                int countPro = 1;

                for (int i = 0; i <= nam; i++) {
                        countSum = countSum + i;
                }

                System.out.print("Треугольное число: " + countSum);
                System.out.print("\n");

                for (int i = 1; i <= nam; i++) {
                        countPro = countPro * i;
                }

                System.out.print("Факториал: " + countPro);

}
}