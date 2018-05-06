from src.Database.SqlServerDb import SqlServerDb
from src.Models.Person import Person


class PersonDAO:

    def __init__(self):
        self._Db_ = SqlServerDb()

    def _toList_(self, pTuple):
        result = list()

        for item in pTuple:
            person = Person()
            person.Id = item.Id
            person.DateOfCreation = item.DateOfCreation
            person.DateOfUpdate = item.DateOfUpdate
            person.BirthDay = item.BirthDay
            person.Name = item.Name
            person.LastName = item.LastName

            result.append(person)

        return result

    def listAll(self):
        query = "SELECT * FROM [dbo].[Person]"
        list = self._Db_.executeQuery(query)

        if list:
            return self._toList_(list)

    def add(self, pEntity):
        guid = self._Db_.getId()
        query = " INSERT INTO Person(Id, Name, LastName, BirthDay)"
        query = ("{} VALUES('{}', '{}', '{}')".format(query,
                                                      guid,
                                                      pEntity.Name,
                                                      pEntity.LastName,
                                                      pEntity.BirthDay))

        self._Db_.executeNonQuery(query)
