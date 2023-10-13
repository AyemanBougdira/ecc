#Exo11

class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.price} and {self.weight}"
    


def get_item():
    price = input('Price:')
    weight = input('Weight')
    return Item(price, weight)

def main():
    item = get_item()
    print(item)

print(Item(4,5))

