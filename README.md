# AirBnB clone - The console

<p align="center">
<img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="texto alternativo" width="400px">
</p>

### Unittest
In order to ensure the quality of this code, I have created a suite of unit tests using Python's built-in unittest module. Please feel free to contribute your own test cases or suggest improvements to the existing tests. Let's work together to make this code as reliable as possible!

### Python Packages Concept Page
In order to better understand how to use and distribute Python packages, I have created a concept page that outlines the key concepts and best practices for working with packages in Python. You can find this page in the "docs" folder of this repository.

### Serialization/Deserialization
Serialization and deserialization are essential concepts when working with data in Python. In this repository, you will find a number of functions that can help you serialize and deserialize data in various formats, including JSON and YAML.
### *args and **kwargs
Python's *args and **kwargs syntax can be a bit confusing at first, but they are incredibly useful for creating flexible functions that can accept any number of arguments or keyword arguments. In this repository, you will find several examples of how to use *args and **kwargs effectively.

### Datetime
Python's datetime module is a powerful tool for working with dates and times. In this repository, you will find a number of functions that can help you manipulate and format dates and times, as well as examples of how to use these functions in your own code.


## The console

The initial step involves creating a data model and then utilizing a console or command interpreter to manage the objects by creating, updating, destroying them, and performing other necessary actions. The objects will be stored and persisted to a JSON file, with a focus on building a powerful storage system that creates an abstraction layer between the objects and their storage and persistence. This ensures that you don't have to worry about how the objects are stored, either in the console code or in the front-end and RestAPI you will build later. This abstraction layer makes it easy to change the storage type without the need to update your entire codebase. The console will serve as a validation tool for the storage engine.
