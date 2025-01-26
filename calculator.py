def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total + 5.99 #adding shipping fee