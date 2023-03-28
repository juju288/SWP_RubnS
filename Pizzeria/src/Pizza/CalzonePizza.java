package src.Pizza;

public class CalzonePizza extends PizzaAbstract {
    @Override
    public void prepare() {

        this.text = this.getClass().getName();
    }

    public String toString() {
        return "CalzonePizza";
    }
}
