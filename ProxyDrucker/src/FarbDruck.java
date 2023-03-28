public class FarbDruck implements Drucker {

    @Override
    public void drucken(String document) {
        System.out.println("Drucke mit Farbe: " + document);

    }
}