import json
import os
from typing import Union

# This is a WIP database for the Python

class load(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
       if os.path.exists(location):
           self._load()
       else:
            self.db = {}
       return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dump(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , key: Union[str, int] , value):
        try:
            self.db[key] = value
            self.dump()
            return True
        except:
            return False

    def get(self , key: Union[str, int]):
        try:
            return print(self.db[key])
        except KeyError:
            print("No Value Can Be Found for " + str(key))
            return False

    def get_two(self, key, value):
        if key in self.db:
            if self.db[key] == value:
                return True
            else:
                return False
        else:
            return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dump()
        return True
    
    def resetdb(self):
        self.db={}
        self.dump()
        return True

    def loadall(self):
        if not self.db:
            print("No Values Found")
            return False
        else:
            print(self.db)
            return True