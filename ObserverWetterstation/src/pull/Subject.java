package pull;

public interface Subject {
    void registriereObserver(Observer observer);
    void entferneObserver(Observer observer);
    void benachrichtigeObserver();
    float getTemperatur();
    float getFeuchtigkeit();
}
