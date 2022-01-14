class Product:
    id: int
    name: str
    price: float
    image: str

    def __init__(self, name, price, image, id = 0):
        self.id = id
        self.name = name
        self.price = price
        self.image = image