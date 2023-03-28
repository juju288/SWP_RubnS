package src.Restaurants;

import src.Pizza.HawaiiPizza;
import src.Pizza.SalamiPizza;
import src.Pizza.TonnoPizza;

public class RostockPizzeria extends PizzaFactory {
    public RostockPizzeria() {
        super(
                new SalamiPizza(),
                new HawaiiPizza(),
                new TonnoPizza()
        );
    }
}
