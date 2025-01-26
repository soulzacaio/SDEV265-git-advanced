from calculator import calculate_total

def test_calculate_total():
    class Item:
        def __init__(self, price):
            self.price = price
    
    items = [Item(10.00), Item(20.00)]
    total = calculate_total(items)
    expected = (30.00 * 1.08) + 5.99  # tax and shipping
    assert abs(total - expected) < 0.01