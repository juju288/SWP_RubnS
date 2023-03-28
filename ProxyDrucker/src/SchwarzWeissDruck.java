public class SchwarzWeissDruck implements Drucker{

    @Override
    public void drucken(String text) {
        System.out.println("Drucke in Schwarz und Weiss: " + text);

    }
}
