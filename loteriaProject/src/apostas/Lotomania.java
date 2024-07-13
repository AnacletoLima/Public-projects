package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Lotomania {
    public void NumerosDaLotomania() {
        ArrayList<Integer> lo = new ArrayList<Integer>();
        for (int c = 0; c < 50; c++) {
            lo.add((int) (Math.random() * 100));
            for (int d = 0; d < lo.size(); d++) {
                for (int e = d + 1; e < lo.size(); e++) {
                    if (lo.get(d).equals(lo.get(e))) {
                        lo.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(lo);
        String lo2 = lo.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + lo2 + ".");
    }
}
