from datetime import datetime


class EntityBase:

    def __init__(self):
        self.Id = None
        self.DateOfCreation = datetime.now()
        self.DateOfUpdate = None
