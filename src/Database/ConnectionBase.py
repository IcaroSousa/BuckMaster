import pyodbc


class ConnectionBase:

    def __init__(self, pServer, pPort, pDatabase, pUser, pPassword):
        self._Server = pServer
        self._Port = pPort
        self._Database = pDatabase
        self._User = pUser
        self._Password = pPassword

        self.__Connection__ = pyodbc.connect(self._getConnectionString())
        self.__Query__ = self.__Connection__.cursor()

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

    def executeQuery(self, pQueryString):
        self.__Query__.execute(pQueryString)
        return self.__Query__.fetchall()

    def executeScalar(self, pQueryString):
        self.__Query__.execute(pQueryString)
        return self.__Query__.fetchval()

    def executeNonQuery(self, pQueryString):
        self.__Query__.execute(pQueryString)
        self.__Connection__.commit()
