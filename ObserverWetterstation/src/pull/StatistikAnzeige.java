package pull;

public class StatistikAnzeige implements Observer {
    private Subject subject;
    private float maxTemp = 0.0f;
    private float minTemp = 200;
    private float tempSum= 0.0f;
    private int anzMesswerte;

    public StatistikAnzeige(Subject subject) {
        this.subject = subject;
        subject.registriereObserver(this);
    }

    public void aktualisieren() {
        float temp = subject.getTemperatur();
        float feucht = subject.getFeuchtigkeit();

        tempSum += temp;
        anzMesswerte++;

        if (temp > maxTemp) {
            maxTemp = temp;
        }

        if (temp < minTemp) {
            minTemp = temp;
        }

        anzeigen(temp, feucht);
    }

    public void anzeigen(float temp, float feucht) {
        System.out.println("Mit/Max/Min Temperatur = " + (tempSum / anzMesswerte)
                + "/" + maxTemp + "/" + minTemp);
    }
}
