# WTS
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

[![Pypi](https://img.shields.io/badge/VERSION-1.0.1-blue?style=for-the-badge&logo=pypi)](https://pypi.org/project/wts/)

``wts`` is a tiny python package which provides a simple way to write in `sqlite` files with `sql` files.

Use ``pip`` to install:
```bash
pip install wts
```

Here is a simple example:

```python
from wts import wts
# intialize the Wts object

wr = wts.Wts("cows.sqlite")
wr.execute_sql_file("cows_data.sql")
# cows.sqlite in filled with the data from cows_data.sql

# OR you can do it like this:
wts.Wts("cows.sqlite").execute_sql_file("cows_data.sql")

```

### WARNINGS :

- Yours sql files must be in the same directory as the database file

- If the slite file does not exist, it will be created

If you have any issues, please open an issue [Here](https://github.com/Chaton-mechant/WTS/issues)
