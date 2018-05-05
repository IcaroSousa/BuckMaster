from src.DAO.PersonDAO import PersonDAO
from src.Models import Person

from datetime import datetime

if __name__ == '__main__':

    person = Person.Person()
    print(person.DateOfCreation)
    person.Name = "Icaro"
    person.LastName = "Sousa"
    person.Id = 10

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