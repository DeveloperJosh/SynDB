# SynDB

[![Downloads](https://pepy.tech/badge/syndb)](https://pepy.tech/project/syndb)
[![Downloads](https://pepy.tech/badge/syndb/month)](https://pepy.tech/project/syndb)
[![Downloads](https://pepy.tech/badge/syndb/week)](https://pepy.tech/project/syndb)
[![SynDB](https://snyk.io/advisor/python/SynDB/badge.svg)](https://snyk.io/advisor/python/SynDB)

## Usage

You can use SynDB to store and retrieve data in a database, And it is very easy to use.

## Description

SynDB is a database that is json based, It is lightweight and fast, And it is easy to use.

## Getting Started

### Dependencies

* [Python](https://www.python.org/downloads/)
### Installing

```py
$ pip install syndb
```

### Exmaple

```python
import syndb

db = syndb.load("test.db", False)

db.set("key", "value")
db.get("key")
db.delete("key")
db.resetdb()
db.dump() 
db.loadall() # This will load all the data from the file
```

## Authors

Contributors names and contact info

DeveloperJosh
[discord](https://discord.gg/321750582912221184)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details