package src.Pizza;

public class TonnoPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();
    }

    public String toString() {
        return "TonnoPizza";
    }
}
