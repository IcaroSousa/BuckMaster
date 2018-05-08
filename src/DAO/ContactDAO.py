from src.Database.SqlServerDb import SqlServerDb
from src.Models.Contact import Contact


class ContactDAO(SqlServerDb):

    def __init__(self):
        super().__init__()

    def _toList_(self, pTuple):
        result = list()

        for item in pTuple:
            contact = Contact()
            contact.Id = item.Id
            contact.DateOfCreation = item.DateOfCreation
            contact.DateOfUpdate = item.DateOfUpdate
            contact.ContactType = item.ContactTypeId
            contact.IdPerson = item.IdPerson
            contact.Contact = item.Contact
            #contact.Placeholder = item.Placeholder

            result.append(contact)

        return result

    def listAll(self):
        query = "SELECT * FROM Contact"
        list = self.executeQuery(query)

        if list:
            return self._toList_(list)

    def add(self, pEntity):
        _query = "INSERT INTO Contact(IdPerson, ContactTypeId, Contact, State) VALUES ('{}', '{}', '{}', '{}')"\
            .format(pEntity.IdPerson, pEntity.ContactType.Id, pEntity.Contact, pEntity.State)

        self.executeNonQuery(_query)
