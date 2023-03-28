package src.Restaurants;

import src.Pizza.CalzonePizza;
import src.Pizza.QuattroPizza;
import src.Pizza.SalamiPizza;

public class HamburgPizzeria extends PizzaFactory {
    public HamburgPizzeria(){
        super(
                new SalamiPizza(),
                new CalzonePizza(),
                new QuattroPizza()
        );
    }
}
