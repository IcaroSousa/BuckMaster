from src.DAO.ContactTypeDAO import ContactTypeDAO
from src.DAO.PersonDAO import PersonDAO

if __name__ == '__main__':

    personDao = PersonDAO()
    contactTypeDao = ContactTypeDAO()

    personlist = list(personDao.listAll())

    if personlist:
        for per in personlist:
            print("Id -> {} Name ->{}".format(per.Id, per.Name))

    contactTypeList = contactTypeDao.listAll()

    if contactTypeList:
        for cont in contactTypeList:
            print("Id -> {} Name -> {}, Description -> {}".format(cont.Id, cont.Description, cont.Description))
