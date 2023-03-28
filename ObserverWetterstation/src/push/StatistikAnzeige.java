package push;

public class StatistikAnzeige implements Observer {
    private float maxTemp = 0.0f;
    private float minTemp = 200;
    private float tempSum= 0.0f;
    private int anzMesswerte;

    public StatistikAnzeige(WetterDaten wetterDaten) {
        wetterDaten.registriereObserver(this);
    }

    public void aktualisieren(float temp, float feucht) {
        tempSum += temp;
        anzMesswerte++;

        if (temp > maxTemp) {
            maxTemp = temp;
        }

        if (temp < minTemp) {
            minTemp = temp;
        }

        anzeigen();
    }

    public void anzeigen() {
        System.out.println("Mit/Max/Min Temperatur = " + (tempSum / anzMesswerte)
                + "/" + maxTemp + "/" + minTemp);
    }
}
