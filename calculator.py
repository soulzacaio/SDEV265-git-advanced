def calculate_total(items):
    total = 0
    for item in items:
        total += item.price

    total *= 1.08  #Adding 8% tax.
    total += 5.99 #adding shipping fee
    return total