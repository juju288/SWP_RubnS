public class main {

    public static void main(String[] args) {
        Drucker schwarzweissdrucker = new SchwarzWeissDruck();
        Drucker farbdrucker = new FarbDruck();

        schwarzweissdrucker.drucken("Hallo");

        farbdrucker.drucken("Hallo in Farbe");

        }
}
