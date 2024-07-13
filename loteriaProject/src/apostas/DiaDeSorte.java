package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class DiaDeSorte {
    public void NumerosDoDiaDeSrote() {
        ArrayList<Integer> dds = new ArrayList<Integer>();
        for (int c = 0; c < 7; c++) {
            dds.add((int) (1 + (Math.random() * 31)));
            for (int d = 0; d < dds.size(); d++) {
                for (int e = d + 1; e < dds.size(); e++) {
                    if (dds.get(d).equals(dds.get(e))) {
                        dds.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(dds);
        String dds2 = dds.stream().map(Object::toString).collect(Collectors.joining(", "));

        int dds3 = (int) (1 + (Math.random() * 12));
        String dds4 = null;
        switch (dds3) {
            case 1:
                dds4 = "Janeiro";
                break;
            case 2:
                dds4 = "Fevereiro";
                break;
            case 3:
                dds4 = "Março";
                break;
            case 4:
                dds4 = "Abril";
                break;
            case 5:
                dds4 = "Maio";
                break;
            case 6:
                dds4 = "Junho";
                break;
            case 7:
                dds4 = "Julho";
                break;
            case 8:
                dds4 = "Agosto";
                break;
            case 9:
                dds4 = "Setembro";
                break;
            case 10:
                dds4 = "Outubro";
                break;
            case 11:
                dds4 = "Novembro";
                break;
            case 12:
                dds4 = "Dezembro";
                break;
        }

        System.out.println("Numeros da sorte: " + dds2 + ".");
        System.out.println("Mes da sorte: " + dds4 + ".");
    }
}
