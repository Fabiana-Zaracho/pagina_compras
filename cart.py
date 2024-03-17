
class Cart:
    from ownable import set_owner
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items
        

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner and hasattr(self.owner, 'wallet') and self.owner.wallet.balance >= self.total_amount():
            # Realizar la compra
            print("Compra realizada con éxito.")
            self.owner.wallet.balance -= self.total_amount()
            self.items = []
        else:
            print("No tienes suficiente saldo para realizar la compra.")

