# WTS
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

[![Pypi](https://img.shields.io/badge/VERSION-0.0.1-blue?style=for-the-badge&logo=pypi)](https://pypi.org/project/wts/)

``wts`` is a tiny python package which provides a simple way to write in `sqlite` files with `sql` insert files.

Use ``pip`` to install:
```
pip install wts
```

Here is a simple example:

```python
from wts import wts

wts.wts("cows_inserts.sql", "cows.sqlite")

# cows.sqlite and cows_inserts.sql are created
```

### WARNINGS :

- Yours commands must be valid sql insert commands

- Yours sql files must be in the same directory as the database file

If you have any issues, please open an issue [Here](https://github.com/Chaton-mechant/WTS/issues)