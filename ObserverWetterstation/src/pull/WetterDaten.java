package pull;

import java.util.ArrayList;

public class WetterDaten implements Subject{
    private float temperatur;
    private float feuchtigkeit;
    ArrayList<Observer> observerList = new ArrayList<Observer>();

    public void registriereObserver(Observer b) {
        observerList.add(b);
    }

    public void entferneObserver(Observer b) {
        int i = observerList.indexOf(b);
        if (i >= 0) {
            observerList.remove(i);
        }
    }

    //temperatur und feuchtigkeit werden nicht mehr in aktualisieren mitgesendet
    public void benachrichtigeObserver() {
        for (Observer observer : observerList) {
            observer.aktualisieren();
        }
    }

    public void geänderteMesswerte() {
        System.out.println(this.toString());
        benachrichtigeObserver();
    }

    public void setMesswerte(float temp, float feucht) {
        this.temperatur = temp;
        this.feuchtigkeit = feucht;
        geänderteMesswerte();
    }

    //Get-Methoden bei Pull notwendig
    public float getTemperatur() {
        return temperatur;
    }

    public float getFeuchtigkeit() {
        return feuchtigkeit;
    }


    public String toString() {
        StringBuffer result = new StringBuffer();
        result.append("#############\n");
        result.append("\nMesswerte:\n");
        result.append("Temperatur: " + getTemperatur() + "\n");
        result.append("Luftfeuchtigkeit: " + getFeuchtigkeit() + "\n");
        return result.toString();
    }
}
