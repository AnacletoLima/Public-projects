package sistema;

import java.util.Scanner;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Main {
    public static int t;

    public static void main(String[] args) {
        boolean validacao;
        Scanner s = new Scanner(System.in);

        do {
            validacao = true;
            System.out.println("Voce sabe o dia em que você quer jogar? Digite 0 para sim e 1 para não.");
            try {
                t = Integer.parseInt(s.nextLine());
                if (t < 0 || t > 1) {
                    throw new IllegalArgumentException();
                }
            } catch (IllegalArgumentException e) {
                System.out.println("\nDesculpe, somente são aceitos os números 0 e 1.\n");
                validacao = false;
            }
        } while (!validacao);

        if (t == 1) {
            int a = (int) (1 + (Math.random() * 29));
            Calendar cal = Calendar.getInstance();
            cal.add(Calendar.DATE, a);
            DateFormat df = new SimpleDateFormat("EEEE dd/MM");
            String nowAsISO = df.format(cal.getTime());
            System.out.println("\nO seu dia de jogar e " + nowAsISO + ".\n");
        } else {
            System.out.println("\nTudo bem. Segue o programa.\n");
        }

        do {
            validacao = true;
            System.out.println("Quantos jogos voce quer fazer? Digite um número entre 1 e 9.");
            try {
                t = Integer.parseInt(s.nextLine());
                if (t < 1 || t > 9) {
                    throw new IllegalArgumentException();
                }
            } catch (IllegalArgumentException e) {
                System.out.println("\nDesculpe, o numero minimo de jogos sao dois. Digite um número entre 1 e 9.\n");
                validacao = false;
            }
        } while (!validacao);

        Logica aposta = new Logica();
        aposta.Jogar();

        System.out.println("\nObrigado por escolher este programa! Pressione a tecla Enter para fechar o programa.");
        s.nextLine();
        s.close();
    }
}