from src.Models.EntityBase import EntityBase


class Person(EntityBase):

    def __init__(self):
        super().__init__()
        self.Name = None
        self.LastName = None
        self.BirthDay = None
        self.DocumentList = None
        self.ContactList = None