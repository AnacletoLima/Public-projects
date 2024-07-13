package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class MegaSena {
    public void NumerosDaMegaSena() {
        ArrayList<Integer> ms = new ArrayList<Integer>();
        for (int c = 0; c < 6; c++) {
            ms.add((int) (1 + (Math.random() * 60)));
            for (int d = 0; d < ms.size(); d++) {
                for (int e = d + 1; e < ms.size(); e++) {
                    if (ms.get(d).equals(ms.get(e))) {
                        ms.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(ms);
        String ms2 = ms.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + ms2 + ".");
    }
}
