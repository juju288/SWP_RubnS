public class ProxyDrucker implements Drucker{
    private Drucker aktuellerDrucker = new SchwarzWeissDruck();

    @Override
    public void drucken(String text) {
        aktuellerDrucker.drucken(text);
    }

    public void switchTo(Drucker andererDrucker, String text){
       this.aktuellerDrucker = andererDrucker;
        aktuellerDrucker.drucken(text);
    }
}
