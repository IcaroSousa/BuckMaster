from src.Database import ConnectionBase


class SqlServerDb(ConnectionBase.ConnectionBase):

    def __init__(self):
        self._DBDriver = "{ODBC Driver 17 for SQL Server}"
        super().__init__("smooth.database.windows.net", 1433, "Rockfeller", "icaro", "#$Attack91")

    def executeQuery(self, pQuery):
        self._Query.execute(pQuery)
        return self._Query.fetchall()

    def executeNonQuery(self, pQuery):
        self._Query.execute(pQuery)
        self._Connection.commit()