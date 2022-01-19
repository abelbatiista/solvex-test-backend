class Location:
    id: int
    user: int
    label: str
    adress: str
    street: str
    number: str
    sector: str
    city: str
    province: str
    country: str
    code: str

    def __init__(self, user, label, adress, street, number, sector, city, province, country, code, id = 0):
        self.id = id
        self.user = user
        self.label = label
        self.adress = adress
        self.street = street
        self.number = number
        self.sector = sector
        self.city = city
        self.province = province
        self.country = country
        self.code = code
