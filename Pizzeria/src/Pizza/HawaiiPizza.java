package src.Pizza;

public class HawaiiPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();
    }

    public String toString() {
        return "HawaiiPizza";
    }
}
