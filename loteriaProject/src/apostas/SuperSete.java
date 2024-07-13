package apostas;

import java.util.ArrayList;
import java.util.stream.Collectors;

public class SuperSete {
    public void NumerosDoSuperSete() {
        ArrayList<Integer> ss = new ArrayList<Integer>();
        for (int c = 0; c < 7; c++) {
            ss.add((int) ((Math.random() * 10)));
        }
        String ss2 = ss.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + ss2 + ".");
    }
}
