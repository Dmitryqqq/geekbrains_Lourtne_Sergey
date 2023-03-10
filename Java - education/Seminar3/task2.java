import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class task2 {
    public static void main(String[] args) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"};
        String[] solarSystem1 = {"mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"};
        ArrayList<String> solarSystemRes = new ArrayList<String>();
        Random rnd = new Random();
        for (int i = 0; i < 10; i++) {
            solarSystemRes.add(solarSystem1[rnd.nextInt(0,7)]);
        }
        System.out.println(solarSystemRes);
        for (int i = 0; i < solarSystem1.length; i++) {
            System.out.printf("%s встречается %d раз \n",solarSystem1[i],Collections.frequency(solarSystemRes, solarSystem1[i]));
        }
    }
}
