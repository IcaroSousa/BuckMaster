from src.Models.EntityBase import EntityBase


class ContactType(EntityBase):

    def __init__(self):
        super().__init__()
        self.Description = None
        self.Placeholder = None
        self.State = None
