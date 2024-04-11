"""Practice Instantiating Pizza Class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)

def price(pizza_order: Pizza) -> float:
    """Calculate and return cost of pizza."""
    if pizza_order.size == "large":
        cost = 6.0
    else:
        cost = 5.0
    # charge 75 cents per topping
    cost += 0.75 * pizza_order.toppings
    # charge 1 dollar if gluten free
    if pizza_order.gluten_free:
        cost += 1.0
    return cost

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())