package push;

import java.util.ArrayList;

public class WetterDaten {
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
    public void benachrichtigeObserver() {
        for (int i = 0; i < observerList.size(); i++) {
            Observer observer = (Observer)observerList.get(i);
            observer.aktualisieren(temperatur, feuchtigkeit);
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
