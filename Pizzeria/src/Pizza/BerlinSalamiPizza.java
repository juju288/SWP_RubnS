package src.Pizza;

public class BerlinSalamiPizza extends SalamiPizza {
    @Override
    public void prepare() {
        this.text = "SpecialBerlin" + this.text;
    }

    public String toString() {
        return "BerlinSalamiPizza";
    }
}
