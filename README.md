# AirBnB clone - The console

<p align="center">
<img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="texto alternativo" width="400px">
</p>

# Important concepts

#### Unittest
In order to ensure the quality of this code, I have created a suite of unit tests using Python's built-in unittest module. Please feel free to contribute your own test cases or suggest improvements to the existing tests. Let's work together to make this code as reliable as possible!
**for example :**
```python
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "La suma debería ser 6")

if __name__ == '__main__':
    unittest.main()
```
#### Datetime

datetime is a Python module to manipulate date, time etc…
In Python, the datetime module provides classes for working with dates and times. The datetime class is the most commonly used class in the datetime module, and it represents a date and time object.
The datetime class has the following attributes:

- **year:** the year (e.g., 2023)
- **month:** the month (1-12)
- **day:** the day of the month (1-31)
- **hour:** the hour (0-23)
- ** minute**: the minute (0-59)
- **second**

for example:
```python
date_string = '2023-02-22T12:34:56.789012'
import datetime
date_string = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
print(date_string)
```
#### Python Packages Concept Page
In order to better understand how to use and distribute Python packages, I have created a concept page that outlines the key concepts and best practices for working with packages in Python. You can find this page in the "docs" folder of this repository.

#### **args and ****kwargs
Python's  **args and ****kwargs syntax can be a bit confusing at first, but they are incredibly useful for creating flexible functions that can accept any number of arguments or keyword arguments. In this repository, you will find several examples of how to use *args and *** kwargs effectively.

**for example : **

```python
def func_iterar(**kwars):
    for key, value in kwars.items():
        print("{} = {}".format(key,value))

func_name = {"name1":"john", "name2" :"pablo" , "name3":"pedro"}
func_iterar(**funcion_name)
```

#### Serialization/Deserialization
Serialization and deserialization are essential concepts when working with data in Python. In this repository, you will find a number of functions that can help you serialize and deserialize data in various formats, including JSON and YAML.
**for example : **
```python
"""Serialization"""

def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

"""Deserialization"""
    def reload(self):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
```

#### Cmd module

The cmd.Cmd class in Python's standard library is a framework for creating command-line interpreters (CLI) with customizable commands and prompts. Its key features include command registration, command parsing, command aliases, prompt customization, command help messages, default command handling, and special command handling.
The cmd.Cmd class also provides default command handling and special command handling for commands such as help, quit, and EOF, which can be customized by defining corresponding do_ methods with the same names.

for example:

```python
import cmd

class MyCmd(cmd.Cmd):
    """Class for an interactive command interpreter"""

    prompt = '>> '

    def do_hello(self, args):
        """Greet the user"""
        print('Hola!')

    def do_exit(self, args):
        """Exits the command interpreter"""
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
```
# The console

The initial step involves creating a data model and then utilizing a console or command interpreter to manage the objects by creating, updating, destroying them, and performing other necessary actions. The objects will be stored and persisted to a JSON file, with a focus on building a powerful storage system that creates an abstraction layer between the objects and their storage and persistence. This ensures that you don't have to worry about how the objects are stored, either in the console code or in the front-end and RestAPI you will build later. This abstraction layer makes it easy to change the storage type without the need to update your entire codebase. The console will serve as a validation tool for the storage engine.

*** see the image: ***
<p align="center">
<img src="https://camo.githubusercontent.com/5a21d91ad4ed61dcc6478878cd9328593c67ae083bdd9fd065b8052d1d428ffc/68747470733a2f2f692e696d6775722e636f6d2f525536376630362e706e67">
</p>


#### Files and Directories
- **models** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- **tests** directory will contain all unit tests.
- **console.py** file is the entry point of our command interpreter.
- **models/base_model.py** file is the base class of all our models. It contains common elements:
 - attributes: **id, created_at** and **updated_at**
 - methods: **save() **and to**_json()**
 
- **models/engine** directory will contain all storage classes (using the same prototype). For the moment you will have only one: **file_storage.py.**

#### Data diagram
<p align="center">
<img src="https://peytonbrsmith.netlify.app/projects/web/airbnb/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5_hu6ccc74028fc11235771a9c9e32891cb9_107677_900x0_resize_q75_box.jpg" alt="texto alternativo" width="700px">
</p>



# Autores

-  Miguel Colmenares([@MiguelColmenares](https://github.com/MiguelColmenares94))
- Marcelo Vizcarra ([@MarceloVizcarra](https://github.com/mavix21))
- John Espino ([@JohnEspino](https://github.com/johnNaduer))

<p align="center">
<a href="https://www.gifsanimados.org/cat-computadora-y-ordenador-56.htm"><img src="https://www.gifsanimados.org/data/media/56/computadora-y-ordenador-imagen-animada-0019.gif" border="0" alt="computadora-y-ordenador-imagen-animada-0019" />
</a>
</p>
