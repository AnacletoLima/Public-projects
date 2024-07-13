package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class DuplaSena {
    public void NumerosDaDuplaSena() {
        ArrayList<Integer> ds = new ArrayList<Integer>();
        for (int c = 0; c < 6; c++) {
            ds.add((int) (1 + (Math.random() * 50)));
            for (int d = 0; d < ds.size(); d++) {
                for (int e = d + 1; e < ds.size(); e++) {
                    if (ds.get(d).equals(ds.get(e))) {
                        ds.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(ds);
        String ds2 = ds.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + ds2 + ".");
    }
}
