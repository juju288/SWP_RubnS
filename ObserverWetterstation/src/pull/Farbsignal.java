package pull;

public class Farbsignal implements Observer {
    private Subject subject;
    
    public Farbsignal(Subject subject) {
        this.subject = subject;
        subject.registriereObserver(this);
    }
    //aktualisieren arbeitet bei Pull nur mit gelieferten Daten über Getter
    @Override
    public void aktualisieren() {
        float temperatur = subject.getTemperatur();
        aktiviereLicht(temperatur);
    }

 
    public void aktiviereLicht(float temperatur) {
        if (temperatur > 50) {
            System.out.println("Rotlicht");
        } else if (temperatur < 0) {
            System.out.println("Blaulicht");
        } else {
            System.out.println("Grünlicht");
        }
    }
}
