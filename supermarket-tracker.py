
class product:
    def __init__(self, name, category, price, quantity, expiry_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self._expiry_date = expiry_date
    def quantity_update():
        print("the quantity was updated")
    def expaire_check():
        print("the expiry date was checked")
    def product_detail():
        print("her is the product detiles")

class enventory:
    def __init__(self, products):
        self.products = products
    def add_new():
        print("a new product was added")
    def update_producte_detail():
        print("the product detail was updated")
    def searsh():
        print("we find the product you searsh about")