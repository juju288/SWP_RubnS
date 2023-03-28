package push;

public class Farbsignal implements Observer {
    private double temperatur;

    //Push-Methode:
    //Temperatur und Luftfeuchtigkeit wereden übergeben und müssen nicht über getter und setter bezogen werden
    //Nachteil vom Push: es werden auch Infos über Luftfeuchtigkeit übergeben, obwohl sie nicht gebraucht werden

    @Override
    public void aktualisieren(float temp, float feucht) {
        this.temperatur = temp;
        aktiviereLicht();
    }


    public void aktiviereLicht() {
        if (temperatur > 50) {
            System.out.println("Rotlicht");
        } else if (temperatur < 0) {
            System.out.println("Blaulicht");
        } else {
            System.out.println("Grünlicht");
        }
    }
}
