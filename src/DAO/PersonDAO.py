from src.Database import SqlServerDb


class PersonDAO:

    def __init__(self):
        self.__Db = SqlServerDb.SqlServerDb()

    def listAll(self):
        query = "SELECT * FROM [dbo].[Person]"
        return self.__Db.executeQuery(query)

    def addPerson(self, pPersonEntity):
        query = " INSERT INTO[dbo].[Person](DateOfCreation, DateOfUpdate, Name, LastName, BirthDay)";
        query = ("{} VALUES(GETDATE(), GETDATE(), '{}', '{}', '{}')".format(query,
                                                                            pPersonEntity.Name,
                                                                            pPersonEntity.LastName,
                                                                            pPersonEntity.BirthDay))

        self.__Db.executeNonQuery(query)
