package hw;

import java.util.ArrayList;
import java.util.Random;

//Пусть дан произвольный список чисел. Удалить из него чётные числа.
public class task1 {
    public static void main(String[] args) {
    //объявляю рандом
    Random rnd = new Random();

    //обьявляю пустой список
    ArrayList<Integer> arrayList = new ArrayList<>(10); 

    for (int i = 0; i < 10; i++) {
        arrayList.add(rnd.nextInt(0,10));
    }

    System.out.println(arrayList);

    for (int i = 0; i < arrayList.size(); i++) {
        if(arrayList.get(i) % 2 == 0 || arrayList.get(i) == 0) {
            arrayList.remove(arrayList.get(i));
            i--;
        }
    }

    System.out.println(arrayList);
    }  
}