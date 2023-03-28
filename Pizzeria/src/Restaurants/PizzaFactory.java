package src.Restaurants;

import src.Pizza.PizzaAbstract;

import java.util.HashMap;
import java.util.Map;

public class PizzaFactory {
    private Map<String, PizzaAbstract> menu = new HashMap<String, PizzaAbstract>();
    public PizzaFactory(PizzaAbstract... pizzas) {
        for (int i = 0; i < pizzas.length; i++) {
            this.menu.put(pizzas[i].getClass().getSimpleName().toUpperCase(), pizzas[i]);
        }
    }

    public PizzaAbstract getPizza(String name) {
        return this.menu.get(name.toUpperCase());
    }

}
