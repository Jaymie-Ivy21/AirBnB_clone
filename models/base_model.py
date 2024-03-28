#!/usr/bin/python3
"""

"""
import uuid
from uuid import uuid4
from datetime import datetime


class BaseModel:
  def __init__(self, *args, **kwargs):
    """

    """
    time_form = "%Y-%m-%dT%H:%M:%S.%f"
    if kwargs:
      for key, value in kwargs.item():
        if key == "__class__":
          continue
        elif key == "created_at" or key == "updated_at":
          setattr(self, key, datetime.strptime(value, time_form))
        else:
          setattr(self, key, value)
    else:
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

if __name__ == "__main__":
  my_model = BaseModel()
  my_model.name = "My First Model"
  my_model.my_number = 89
  print(my_model)
  my_model.save()
  print(my_model)
  my_model_json =my_model.to_dict()
  print(my_model_json)
  print("JSON of my_model")
  for key  in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

