package pull;

public class AktuelleBedingungenAnzeige implements Observer {
    //um getter aufrufen zu können
    private Subject subject;

    public AktuelleBedingungenAnzeige(Subject subject) {
        this.subject = subject;
        subject.registriereObserver(this);
    }

    public void aktualisieren() {
        float temp = subject.getTemperatur();
        float feucht = subject.getFeuchtigkeit();
        anzeigen(temp, feucht);
    }

    public void anzeigen(float temp, float feucht) {
        System.out.println("Aktuelle: " + temp
                + " °C und " + feucht + "% Luftfeuchtigkeit");
    }
}
