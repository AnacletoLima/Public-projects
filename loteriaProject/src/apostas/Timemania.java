package apostas;

import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

public class Timemania {
    public void NumerosDaMTimemania() {
        ArrayList<Integer> tm = new ArrayList<Integer>();
        for (int c = 0; c < 10; c++) {
            tm.add((int) (1 + (Math.random() * 80)));
            for (int d = 0; d < tm.size(); d++) {
                for (int e = d + 1; e < tm.size(); e++) {
                    if (tm.get(d).equals(tm.get(e))) {
                        tm.clear();
                        c = -1;
                    }
                }
            }
        }
        Collections.sort(tm);
        String tm2 = tm.stream().map(Object::toString).collect(Collectors.joining(", "));

        ArrayList<String> TimeDoCoracao = new ArrayList<String>();
        TimeDoCoracao.add("ABC");
        TimeDoCoracao.add("Altos");
        TimeDoCoracao.add("America-MG");
        TimeDoCoracao.add("America-RN");
        TimeDoCoracao.add("Aparecidense");
        TimeDoCoracao.add("Athletico");
        TimeDoCoracao.add("Atletico-AC");
        TimeDoCoracao.add("Atletico-CE");
        TimeDoCoracao.add("Atletico-GO");
        TimeDoCoracao.add("Atletico-MG");
        TimeDoCoracao.add("Avai");
        TimeDoCoracao.add("Bahia");
        TimeDoCoracao.add("Boa Esporte");
        TimeDoCoracao.add("Boa Vista");
        TimeDoCoracao.add("Botafogo-PB");
        TimeDoCoracao.add("Botafogo-RJ");
        TimeDoCoracao.add("Botafogo-SP");
        TimeDoCoracao.add("Bragantino");
        TimeDoCoracao.add("Brasil");
        TimeDoCoracao.add("Brasiliense");
        TimeDoCoracao.add("Brusque");
        TimeDoCoracao.add("Campinense");
        TimeDoCoracao.add("Caxias");
        TimeDoCoracao.add("Ceara");
        TimeDoCoracao.add("Chapecoense");
        TimeDoCoracao.add("Cianorte");
        TimeDoCoracao.add("Confianca");
        TimeDoCoracao.add("Corinthians");
        TimeDoCoracao.add("Coritiba");
        TimeDoCoracao.add("CRB");
        TimeDoCoracao.add("Criciuma");
        TimeDoCoracao.add("Cruzeiro");
        TimeDoCoracao.add("CSA");
        TimeDoCoracao.add("Cuiaba");
        TimeDoCoracao.add("Ferroviaria");
        TimeDoCoracao.add("Ferroviario");
        TimeDoCoracao.add("Figueirense");
        TimeDoCoracao.add("Flamengo");
        TimeDoCoracao.add("Floresta");
        TimeDoCoracao.add("Fluminense");
        TimeDoCoracao.add("Fortaleza");
        TimeDoCoracao.add("Goias");
        TimeDoCoracao.add("Gremio");
        TimeDoCoracao.add("Guarani");
        TimeDoCoracao.add("Imperatriz");
        TimeDoCoracao.add("Internacional");
        TimeDoCoracao.add("Ituano");
        TimeDoCoracao.add("Jacuipense");
        TimeDoCoracao.add("Joinville");
        TimeDoCoracao.add("Juazeirense");
        TimeDoCoracao.add("Juventude");
        TimeDoCoracao.add("Londrina");
        TimeDoCoracao.add("Luverdense");
        TimeDoCoracao.add("Manaus");
        TimeDoCoracao.add("Mirasol");
        TimeDoCoracao.add("Moto Club");
        TimeDoCoracao.add("Nautico");
        TimeDoCoracao.add("Novorizontino");
        TimeDoCoracao.add("Oeste");
        TimeDoCoracao.add("Operario");
        TimeDoCoracao.add("Palmeiras");
        TimeDoCoracao.add("Parana");
        TimeDoCoracao.add("Paysandu");
        TimeDoCoracao.add("Ponte Preta");
        TimeDoCoracao.add("Remo");
        TimeDoCoracao.add("Sampaio Correa");
        TimeDoCoracao.add("Santa Cruz");
        TimeDoCoracao.add("Santos");
        TimeDoCoracao.add("Sao Bento");
        TimeDoCoracao.add("Sao Jose");
        TimeDoCoracao.add("Sao Paulo");
        TimeDoCoracao.add("Sao Raimundo");
        TimeDoCoracao.add("Sport Recife");
        TimeDoCoracao.add("Tombense");
        TimeDoCoracao.add("Treze");
        TimeDoCoracao.add("Vasco da Game");
        TimeDoCoracao.add("Vila Nova");
        TimeDoCoracao.add("Vitoria");
        TimeDoCoracao.add("Volta Redonda");
        TimeDoCoracao.add("Ypiranga");

        System.out.println("Numeros da sorte: " + tm2 + ".");
        String tm3 = TimeDoCoracao.get((int) (Math.random() * 80));
        System.out.println("Time do coracao: " + tm3 + ".");
    }
}
