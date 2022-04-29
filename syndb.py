import json
import os
import signal
import sys
from typing import Union
from threading import Thread


def load(location, auto_dump):
    return SynDB(location, auto_dump)

class SynDB(object):

    key_error = TypeError('Key/name must be a string!')

    def __init__(self , location, auto_dump):
        self.location = os.path.expanduser(location)
        self.load(self.location, auto_dump)
        self.dthread = Thread(target=self._autodump)
        if auto_dump is True:
            self.dthread.start()
        self.set_sigterm_handler()

    def load(self , location, auto_dump):
       self.loco = location
       self.auto_dump = auto_dump
       if os.path.exists(location):
           self._load()
       else:
            self.db = {}
       return True

    def _autodump(self):
        if self.auto_dump:
            self.dump()

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def set_sigterm_handler(self):
         def sigterm_handler():
            if self.dthread is not None:
                self.dthread.join()
            sys.exit(0)
         signal.signal(signal.SIGTERM, sigterm_handler)

    def dump(self):
        try:
            json.dump(self.db, open(self.location, "w"))
            self.dthread = Thread(
            target=json.dump,
            args=(self.db, open(self.loco, 'wt')))
            self.dthread.start()
            self.dthread.join()
            return True
        except:
            return False

    def set(self , key, value):
        if isinstance(key, str):
            self.db[key] = value
            self._autodump()
            return True
        else:
            raise self.key_error

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