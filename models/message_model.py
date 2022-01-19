class Message:
    id: int
    frm: str
    to: str
    message: str
    date: str


    def __init__(self, frm, to, message, date, id = 0):
        self.id = id
        self.frm = frm
        self.to = to
        self.message = message
        self.date = date
