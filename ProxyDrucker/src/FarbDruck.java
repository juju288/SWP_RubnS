public class FarbDruck implements Drucker {

    @Override
    public void drucken(String text) {
        System.out.println("Drucke mit Farbe: " + text);

    }
}
