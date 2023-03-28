package src.Pizza;

public class SalamiPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();
    }

    public String toString() {
        return "SalamiPizza";
    }
}
