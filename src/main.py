from src.DAO.PersonDAO import PersonDAO
from src.Models import Person

from datetime import datetime

if __name__ == '__main__':

    person = Person.Person()
    person.Name = "Icaro"
    person.LastName = "Sousa"
    person.BirthDay = datetime(1992, 10, 5).date()
    person.DateOfCreation = datetime.now().date()
    person.DateOfUpdate = datetime.now().date()

    personDao = PersonDAO()
    list = personDao.listAll()

    if len(list) > 0:
        for item in list:
            print("Id -> {} Name ->{}".format(item[0], item[3]))

    personDao.addPerson(person)
    list = personDao.listAll()

    if len(list) > 0:
        for item in list:
            print("Id -> {} Name ->{}".format(item[0], item[3]))