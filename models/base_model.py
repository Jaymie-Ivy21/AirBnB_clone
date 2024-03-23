#!/usr/bin/python3
"""

"""
import uuid
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
  def __init__(self):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.today()
    self.updated_at = datetime.today()

  def save(self):
    """

    """
    self.updated_at = datetime.today()

  def to_dict(self):
    """

    """
    ins_dict = self.__dict__.copy()
    ins_dict["__class__"] = self.__class__.__name__
    ins_dict["created_at"] = self.created_at.isoformat()
    ins_dict["updated_at"] = self.updated_at.isoformat()
    return ins_dict

  def __str__(self):
    """
    
    """
    class_name = self.__class__.__name__
    return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

