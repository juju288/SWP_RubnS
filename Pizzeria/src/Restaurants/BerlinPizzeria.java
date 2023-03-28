package src.Restaurants;

import src.Pizza.BerlinSalamiPizza;
import src.Pizza.HawaiiPizza;
import src.Pizza.SalamiPizza;
import src.Pizza.TonnoPizza;

public class BerlinPizzeria extends PizzaFactory {
    public BerlinPizzeria() {
        super(
                new BerlinSalamiPizza(),
                new SalamiPizza(),
                new TonnoPizza(),
                new HawaiiPizza()
        );
    }
}
