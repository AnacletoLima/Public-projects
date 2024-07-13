package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class MaisMilionaria {
    public void NumerosDaMaisMilionaria() {
        ArrayList<Integer> mm = new ArrayList<Integer>();
        for (int c = 0; c < 6; c++) {
            mm.add((int) (1 + (Math.random() * 50)));
            for (int d = 0; d < mm.size(); d++) {
                for (int e = d + 1; e < mm.size(); e++) {
                    if (mm.get(d).equals(mm.get(e))) {
                        mm.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(mm);
        String mm2 = mm.stream().map(Object::toString).collect(Collectors.joining(", "));

        ArrayList<Integer> mm3 = new ArrayList<Integer>();
        for (int c = 0; c < 2; c++) {
            mm3.add((int) (1 + (Math.random() * 6)));
            for (int d = 0; d < mm3.size(); d++) {
                for (int e = d + 1; e < mm3.size(); e++) {
                    if (mm3.get(d).equals(mm3.get(e))) {
                        mm3.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(mm3);
        String mm4 = mm3.stream().map(Object::toString).collect(Collectors.joining(", "));

        System.out.println("Numeros da sorte: " + mm2 + ".");
        System.out.println("Trevos da sorte: " + mm4 + ".");
    }
}
