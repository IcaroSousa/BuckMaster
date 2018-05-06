from src.Database.SqlServerDb import SqlServerDb
from src.Models.ContactType import ContactType


class ContactTypeDAO:

    def __init__(self):
        self._Db_ = SqlServerDb()

    def _toList_(self, pTuple):
        result = list()

        for item in pTuple:
            contactType = ContactType()
            contactType.Id = item.Id
            contactType.DateOfCreation = item.DateOfCreation
            contactType.DateOfUpdate = item.DateOfUpdate
            contactType.Description = item.Description
            contactType.Placeholder = item.Placeholder
            contactType.State = item.State

            result.append(contactType)

        return result

    def listAll(self):
        query = "SELECT * FROM ContactType"
        list = self._Db_.executeQuery(query)

        if list:
            return self._toList_(list)

    def add(self, pEntity):
        _query = " INSERT INTO ContactType(Description, Placeholder, State) VALUES ('{}', '{}', '{}')" \
            .format(pEntity.Description, pEntity.Placeholder, pEntity.State)

        self._Db_.executeNonQuery(_query)
