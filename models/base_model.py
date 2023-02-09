#!/usr/bin/python3
"""Definition of the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """This represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()
        if len(kwargs) != 0:
            for k, v in kwargs.item():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the BaseModel instance dictionary
        It includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["updates_at"] = self.updated_at.isoformat()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the print/str represenation for the BaseModel instance"""
        clname = self.__class__.name
        return "[{}] ({}) {}".format(clname, sel.id, self.__dict__)
