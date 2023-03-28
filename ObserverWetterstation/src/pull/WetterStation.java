package pull;

public class WetterStation {

    public static void main(String[] args) {
        WetterDaten wetterDaten = new WetterDaten();

        AktuelleBedingungenAnzeige aktuelleAnzeige = new AktuelleBedingungenAnzeige(wetterDaten);
        StatistikAnzeige statistikAnzeige = new StatistikAnzeige(wetterDaten);
        Farbsignal farbsignal = new Farbsignal(wetterDaten);

        wetterDaten.setMesswerte(-3, 65);
        wetterDaten.setMesswerte(32, 70);
        wetterDaten.setMesswerte(55, 90);
    }
}
