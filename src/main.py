from src.DAO.ContactDAO import ContactDAO
from src.DAO.ContactTypeDAO import ContactTypeDAO
from src.DAO.PersonDAO import PersonDAO
from src.Models.Contact import Contact

if __name__ == '__main__':

    personDao = PersonDAO()
    contactTypeDao = ContactTypeDAO()
    contactDao = ContactDAO()

    personlist = list(personDao.listAll())

    if personlist:
        for per in personlist:
            print("Id -> {} Name ->{}".format(per.Id, per.Name))

    contactTypeList = contactTypeDao.listAll()

    if contactTypeList:
        for cont in contactTypeList:
            print("Id -> {} Name -> {}, Description -> {}".format(cont.Id, cont.Description, cont.Description))

    contact = Contact()
    contact.Contact = "(62)98461-1439"
    contact.Placeholder = "(\d{2})(\d{4,5})-(\d{4})"
    contact.State = "A"
    contact.ContactType = contactTypeList.pop()
    contact.IdPerson = personlist.pop().Id

    contactDao.add(contact)

    contactList = contactDao.listAll()
    for ctt in contactList:
        print("Contato -> {}".format(ctt.Contact))
