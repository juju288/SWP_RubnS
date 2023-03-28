package src;

import src.Pizza.PizzaAbstract;
import src.Pizza.SalamiPizza;
import src.Restaurants.BerlinPizzeria;
import src.Restaurants.HamburgPizzeria;
import src.Restaurants.PizzaFactory;

import java.util.HashMap;
import java.util.Map;

public class main {
    private static Map<String, String> test = new HashMap<String, String>();

    public static void main(String[] args) {
        PizzaFactory hp = new HamburgPizzeria();
        PizzaAbstract sp = new SalamiPizza();
        System.out.println("Hat " + hp.getClass().getSimpleName() + " Salami Pizza?");
        System.out.println("Ja, sie hat " + sp.toString());
        sp.bake();
        sp.cut();
        sp.boxedUp();
        System.out.println(sp.toString()+"ist fertig");
    }
}
