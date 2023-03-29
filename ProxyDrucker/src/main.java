public class main {

    public static void main(String[] args) {
        ProxyDrucker meinDrucker = new ProxyDrucker();

        meinDrucker.drucken("Hallo");
        meinDrucker.switchTo(new FarbDruck(), "Hallo in Farbe");
        meinDrucker.switchTo(new SchwarzWeissDruck(), "Hallo in Schwarz");

        }
}
