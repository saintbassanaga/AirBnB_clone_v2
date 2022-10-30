#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import os


def all_main() -> object:
    """ return dictionary objects """
    return FileStorage.__objects


def new(obj):
    """ sets in dictionary the obj with key <obj class name>.id """
    FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj


def save():
    """ serializes objects to the JSON file (path: __file_path) """
    with open(FileStorage.__file_path, 'w', encoding='utf-8') as fName:
        new_dict = {key: obj.to_dict() for key, obj in
                    FileStorage.__objects.items()}
        json.dump(new_dict, fName)


def reload():
    """ Reload the file """
    if os.path.isfile(FileStorage.__flags__):
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as fName:
            l_json = json.load(fName)
            for key, val in l_json.items():
                FileStorage.__objects[key] = eval(
                    val['__class__'])(**val)


class FileStorage:
    """ construct """
    __objects = None
    __file_path = "file.json"
