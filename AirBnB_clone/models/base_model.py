#!/usr/bin/python3
"""Defines a class BaseModel"""
import uuid
from datetime import datetime

class BaseModel:
    """A class representation for all attributes
    and methods of BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Initiaalizes the BaseModel class
        Args:
            args: A variable arguments
            kwargs: A variable keyword arguments
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        print(BaseModel, self.id, self.__dict__)
