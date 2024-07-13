package sistema;

import java.util.ArrayList;
import apostas.*;

public class Logica extends Main {
    public void Jogar() {

        ArrayList<String> apostas = new ArrayList<String>();
        apostas.add("Dia de Sorte");
        apostas.add("Dupla-Sena");
        apostas.add("Lotofacil");
        apostas.add("Lotomania");
        apostas.add("+Milionaria");
        apostas.add("Mega-Sena");
        apostas.add("Quina");
        apostas.add("Super sete");
        apostas.add("Timemania");

        ArrayList<Integer> ms = new ArrayList<Integer>();

        for (int c = 0; c < t; c++) {
            ms.add((int) ((Math.random() * 9)));
            for (int d = 0; d < ms.size(); d++) {
                for (int e = d + 1; e < ms.size(); e++) {
                    if (ms.get(d).equals(ms.get(e))) {
                        ms.clear();
                        c = -1;
                    }
                }
            }
        }

        Integer[] array = ms.toArray(new Integer[0]);
        for (Integer n : array) {
            System.out.println("\n" + apostas.get(n));
            switch (n) {
                case 0:
                    DiaDeSorte sorte = new DiaDeSorte();
                    sorte.NumerosDoDiaDeSrote();
                    break;
                case 1:
                    DuplaSena dupla = new DuplaSena();
                    dupla.NumerosDaDuplaSena();
                    break;
                case 2:
                    Lotofacil loto = new Lotofacil();
                    loto.NumerosDaLotofacil();
                    break;
                case 3:
                    Lotomania lotom = new Lotomania();
                    lotom.NumerosDaLotomania();
                    break;
                case 4:
                    MaisMilionaria milionaria = new MaisMilionaria();
                    milionaria.NumerosDaMaisMilionaria();
                    break;
                case 5:
                    MegaSena mega = new MegaSena();
                    mega.NumerosDaMegaSena();
                    break;
                case 6:
                    Quina quina = new Quina();
                    quina.NumerosDaQuina();
                    break;
                case 7:
                    SuperSete superSete = new SuperSete();
                    superSete.NumerosDoSuperSete();
                    break;
                case 8:
                    Timemania time = new Timemania();
                    time.NumerosDaMTimemania();
                    break;
            }
        }
    }
}
