def total_cost (price, quantity, discount):
    subtotal = price * quantity
    subtotal = subtotal * (1 - discount)
    tax = subtotal * 0.15
    return subtotal + tax

print("The total cost is", total_cost(10,3,0.2))