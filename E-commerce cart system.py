class Ecart:
    def __init__(self, customer):
        self.customer = customer
        self.products = {}

    def add_product(self, product_name, price):
        if price < 0:
            print("The value of price you entered is not a valid value")
        else:
            self.products[product_name] = price
            print(f"Added {product_name} : {price} Rupees")

    def remove_product(self, product_name):
        if not self.products:
            print("There is nothing in the cart, It is empty")
        else:
            removed = self.products.pop(product_name, None)
            if removed is None:
                print(f"{product_name} is not in the cart")
            else:
                print(f'The removed product from cart is {product_name} : {removed} Rupees')

    def total_amount(self):
        total = sum(self.products.values())
        print(f'The total amount payable by {self.customer} is {total} Rupees only ')
        return total

    def display(self):
        if not self.products:
            print("The cart is empty, There is nothing to display")
        else:
            print(f"Cart of {self.customer}:")
            for product, price in self.products.items():
                print(f' - {product} : {price} Rupees')



customer1 = Ecart("Virat")
customer1.add_product("mobile", 20000)
customer1.add_product("sony television", 50000)
customer1.total_amount()
customer1.display()
customer1.remove_product("mobile")
customer1.display()
