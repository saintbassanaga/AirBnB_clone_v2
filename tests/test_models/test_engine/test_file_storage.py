#!/usr/bin/python3
""" Check Filestorage class """
import unittest
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_storage(unittest.TestCase):
    """ check the class """

    def setUp(self):
        """ check empty """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_no_objs(self):
        """ check empty class  """
        self.assertEqual(all(), {})

    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        obj = all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_save_create(self):
        """ Save  """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(obj, all()[obj_key])
        self.assertEqual(obj1, all()[obj1_key])
        self.assertEqual(obj2, all()[obj2_key])
        self.assertEqual(obj3, all()[obj3_key])
        self.assertEqual(obj4, all()[obj4_key])
        self.assertEqual(obj5, all()[obj5_key])
        self.assertEqual(obj6, all()[obj6_key])

    def test_new_empty(self):
        """ check new method """
        with self.assertRaises(TypeError):
            new()

    def test_new_classes(self):
        """ check  new method is valid """
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(all(), {})
        obj.id = 123
        new(obj)
        new(obj1)
        new(obj2)
        new(obj3)
        new(obj4)
        new(obj5)
        new(obj6)
        self.assertEqual(obj, all()[obj_key])
        self.assertEqual(obj1, all()[obj1_key])
        self.assertEqual(obj2, all()[obj2_key])
        self.assertEqual(obj3, all()[obj3_key])
        self.assertEqual(obj4, all()[obj4_key])
        self.assertEqual(obj5, all()[obj5_key])
        self.assertEqual(obj6, all()[obj6_key])

    def test_reload(self):
        """ check reload classes """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id
        save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        reload()

        self.assertTrue(obj_key in all().keys())
        self.assertEqual(obj.id, all()[obj_key].id)
        self.assertTrue(obj1_key in all().keys())
        self.assertEqual(obj1.id, all()[obj1_key].id)
        self.assertTrue(obj2_key in all().keys())
        self.assertEqual(obj2.id, all()[obj2_key].id)
        self.assertTrue(obj3_key in all().keys())
        self.assertEqual(obj3.id, all()[obj3_key].id)
        self.assertTrue(obj4_key in all().keys())
        self.assertEqual(obj4.id, all()[obj4_key].id)
        self.assertTrue(obj5_key in all().keys())
        self.assertEqual(obj5.id, all()[obj5_key].id)
        self.assertTrue(obj6_key in all().keys())
        self.assertEqual(obj6.id, all()[obj6_key].id)
