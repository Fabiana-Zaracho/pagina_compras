
class Item:
    from ownable import set_owner
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Al crearse una instancia de la clase Item, esa instancia de Item (self) se almacena en una variable de clase llamada "instancias".

        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Retorna "instances" ==> Esto significa que al llamar a Item.item_all(), se devuelven todas las instancias de Item que se hayan creado hasta el momento.

        return Item.instances
