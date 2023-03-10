import java.util.ArrayList;
import java.util.Arrays;

public class task3 {
    public static void main(String[] args) {
        ArrayList arrayList = new ArrayList<>(Arrays.asList(1 ,"Venera", 1, 2, "Venera", "Mars", "Jupiter", 2, "Earth"));


        for (int i = arrayList.size() - 1; i >= 0; i--) {
            if (arrayList.get(i) instanceof Integer) {
                arrayList.remove(i);
            }
        }

        System.out.print(arrayList);
    }
}
