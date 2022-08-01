"""
This is the module that provides the base class
BaseModel.
"""

from datetime import datetime
import json
import uuid


class BaseModel():
    """This is a class BaseModel that defines all common
    attributes/methods for other classes.
    """

    def __init__(self):
        """
        init function
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[{}] ({}) {}".format(type(self), self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__
        obj_dict['__class__'] = type(self)
        obj_dict['created_at'] = str(obj_dict['created_at'].isoformat())
        obj_dict['updated_at'] = str(obj_dict['updated_at'].isoformat())
        return obj_dict
