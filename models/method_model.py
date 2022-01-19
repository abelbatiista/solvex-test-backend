class Method:
    id: int
    user: int
    brand: str
    number: str
    expiration: str
    cvv: str

    def __init__(self, user, brand, number, expiration, cvv, id = 0):
        self.id = id
        self.user = user
        self.brand = brand
        self.number = number
        self.expiration = expiration
        self.cvv = cvv
