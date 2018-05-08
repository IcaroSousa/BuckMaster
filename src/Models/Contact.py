from src.Models.EntityBase import EntityBase


class Contact(EntityBase):

    def __init__(self):
        super().__init__()
        self.IdPerson = None
        self.ContactType = None
        self.Placeholder = None
        self.Contact = None
        self.State = None
