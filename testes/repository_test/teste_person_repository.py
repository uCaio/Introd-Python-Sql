from catalogado.model import Person
from catalogado.repository import PersonRepository
from unittest import TestCase

import datetime

class PersonRepositoryTestCase(TestCase):


    def setUp(self):
       self.repository: PersonRepository = PersonRepository()
    
    def test_insert_operation(self):
        person: Person = Person(name ="Caio Marcio Ferreira Gonçalves", nascimento = datetime.datetime(year=1990, month=2, day=1))

        actual_person_count: int = self.repository.count()

        self.assertIsNone(person.id) 
        self.repository.insert(person)
        self.assertIsInstance(person.id, int) 

        new_person_count: int = self.repository.count()
        self.assertEqual(new_person_count, old_person_count + 1)



 