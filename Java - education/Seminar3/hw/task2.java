package hw;

import java.util.ArrayList;
import java.util.Arrays;

//задан целочисленный arrayList. Найти минимальное, максимальное и среднее арифмитич. этого списка.
public class task2 {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<Integer>(Arrays.asList(1, 2, 4, 2));

        System.out.println("Список: " + arrayList);
        System.out.println("Среднее значение: " + mid(arrayList));
        System.out.println("Манимальное значение: " + min(arrayList));
        System.out.println("Максимальное значение: " + max(arrayList));
    }

    public static int mid(ArrayList<Integer> array) {
        int mid = 0;
        int count = 0;
        for (int i = 0; i < array.size(); i++) {
            count += array.get(i);
            mid = count / 2;
        }
        return mid;
    }


    public static int min(ArrayList<Integer> array) {
        int min = array.get(0);
        for (int i = 1; i < array.size() - 1; i++) {
            if(array.get(i) < min) {
                min = array.get(i);
            }
        } 
        return min;
    }

    public static int max(ArrayList<Integer> array) {
        int max = array.get(0);
        for (int i = 1; i < array.size() - 1; i++) {
            if(array.get(i) > max) {
                max = array.get(i);
            }
        } 
        return max;
    }
}
