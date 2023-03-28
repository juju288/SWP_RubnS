package src.Pizza;

public class QuattroPizza extends PizzaAbstract {
    @Override
    public void prepare() {
        this.text = this.getClass().getName();
    }

    public String toString() {
        return "QuattroPizza";
    }
}
