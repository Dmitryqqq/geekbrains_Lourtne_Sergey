public class task2 {
    public static void main(String[] args) {
        int[] arr = new int[1000];

        for (int i = 0; i < arr.length; i++){             
            arr[i] = i+1;   
        }

        for (int i = 1; i < arr.length; i++) {
            if (primeNumber(arr[i]) == 1){
                System.out.print(arr[i]+" ");
            }
        }
}

    private static int primeNumber(int number)
        {
            for (int i=2; i<number; i++)
            {
                if (number%i == 0)
                {
                    return 0;
                }

                if ((i==number) || (i>Math.sqrt(number)))
                {
                    return 1;
                }
            }
            return 0;
        }
}
