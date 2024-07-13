package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Quina {
    public void NumerosDaQuina() {
        ArrayList<Integer> q = new ArrayList<Integer>();
        for (int c = 0; c < 5; c++) {
            q.add((int) (1 + (Math.random() * 80)));
            for (int d = 0; d < q.size(); d++) {
                for (int e = d + 1; e < q.size(); e++) {
                    if (q.get(d).equals(q.get(e))) {
                        q.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(q);
        String q2 = q.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.println("Numeros da sorte: " + q2 + ".");
    }
}
