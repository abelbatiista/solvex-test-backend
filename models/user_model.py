class User:
    id: int
    name: str
    lastname: str
    email: str
    password: str
    role: str
    image: str

    def __init__(self, name, lastname, email, password, role, image, id = 0):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
        self.image = image
