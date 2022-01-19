class Order:
    id: int
    location: int
    method: int
    user: int
    product: int
    order: str

    def __init__(self, location, method, user, product, order, id = 0):
        self.id = id
        self.location = location
        self.method = method
        self.user = user
        self.product = product
        self.order = order
