package push;

public class AktuelleBedingungenAnzeige implements Observer {
    private float temperatur;
    private float feuchtigkeit;

    public AktuelleBedingungenAnzeige(WetterDaten wetterDaten) {
        wetterDaten.registriereObserver(this);
    }

    public void aktualisieren(float temp, float feucht) {
        this.temperatur = temp;
        this.feuchtigkeit = feucht;
        anzeigen();
    }

    public void anzeigen() {
        System.out.println("Aktuelle: " + temperatur
                + " °C und " + feuchtigkeit + "% Luftfeuchtigkeit");
    }
}
