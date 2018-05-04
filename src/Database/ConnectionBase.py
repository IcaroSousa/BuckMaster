import pyodbc


class ConnectionBase:

    def __init__(self, pServer, pPort, pDatabase, pUser, pPassword):
        self._Server = pServer
        self._Port = pPort
        self._Database = pDatabase
        self._User = pUser
        self._Password = pPassword

        self._Connection = pyodbc.connect(self._getConnectionString())
        self._Query = self._Connection.cursor()

    @property
    def _getDriverList(self):
        return pyodbc.drivers()

    def _getConnectionString(self):
        return "DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}".format(self._DBDriver,
                                                                              self._Server,
                                                                              self._Port,
                                                                              self._Database,
                                                                              self._User,
                                                                              self._Password)
