package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Lotofacil {
    public void NumerosDaLotofacil() {
        ArrayList<Integer> l = new ArrayList<Integer>();
        for (int c = 0; c < 15; c++) {
            l.add((int) (1 + (Math.random() * 25)));
            for (int d = 0; d < l.size(); d++) {
                for (int e = d + 1; e < l.size(); e++) {
                    if (l.get(d).equals(l.get(e))) {
                        l.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(l);
        String l2 = l.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + l2 + ".");
    }
}
