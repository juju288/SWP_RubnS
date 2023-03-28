public class SchwarzWeissDruck implements Drucker{

    @Override
    public void drucken(String document) {
        System.out.println("Drucke in Schwarz und Weiss: " + document);

    }
}
