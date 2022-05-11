import json
import os
import signal
import sys
from threading import Thread


def load(location, auto_dump):
    return SynDB(location, auto_dump)

class SynDB(object):

    key_error = TypeError('Key must be a string!')

    def __init__(self , location, auto_dump):
        self.location = os.path.expanduser(location)
        self.load(self.location, auto_dump)
        self.dthread = Thread(target=self._autodump)
        if auto_dump is True:
            self.dthread.start()
        self.set_sigterm_handler()

    def __del__(self):
        if self.dthread is not None:
            self.dthread.join()

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
        try:
            self.db = json.load(open(self.location, "r"))
        except ValueError:
            self.db = {}

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

    def ping(self):
        try:
            self._load()
            return True
        except:
            return False

    def update(self, key, value):
        if key in self.db:
            self.db[key] = value
            self._autodump()
            return True
        else:
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            return False

    def get_all(self):
        return self.db.keys()

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

    def append(self, key, value):
        if not key in self.db:
            self.db[key] = []
        self.db[key].append(value)
        self._autodump()
        return True

    def exists(self, key):
        if key in self.db:
            return True
        else:
            return False

    ## Must read, All of the code under this line is being tested.

    def list_create(self, key):
        if not key in self.db:
            self.db[key] = []
            self._autodump()
            return True
        else:
            return False

    def list_add(self, key, value):
        if key in self.db:
            self.db[key].append(value)
            self._autodump()
            return True
        else:
            return False

    def list_get(self, key):
        if key in self.db:
            return self.db[key]
        else:
            return False

    def list_delete(self, key, value):
        if key in self.db:
            self.db[key].remove(value)
            self._autodump()
            return True
        else:
            return False