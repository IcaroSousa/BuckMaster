from src.Database.ConnectionBase import ConnectionBase


class SqlServerDb(ConnectionBase):

    def __init__(self):
        self._DBDriver = "{ODBC Driver 17 for SQL Server}"
        super().__init__("smooth.database.windows.net", 1433, "Rockfeller", "icaro", "#$Attack91")

    def getId(self):
        return super().executeScalar("SELECT NEWID() AS GUID")

    def executeQuery(self, pQuery):
        return super().executeQuery(pQuery)

    def executeNonQuery(self, pQuery):
        super().executeNonQuery(pQuery)
