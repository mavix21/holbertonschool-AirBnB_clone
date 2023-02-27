#!/usr/bin/python3
""" This module defines the HBNBCommand interpreter """

import cmd
from utils.console_utils import validate_args, parse_args
from utils.common_utils import get_key
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage, classes


class HBNBCommand(cmd.Cmd):
    """ The entry point of the command interpreter """

    intro = "\\o/  Welcome to HBNB command line  \\o/"
    prompt = "(hbnb) "

    def precmd(self, line):
        """ Overrides the default precmd method """

        if all([
            line,
            line[0].isupper(),
            "." in line,
            "(" in line,
            ")" in line,
        ]):
            parts = line.split(".")
            arg1 = parts[0]
            parts = parts[1].split("(")
            command = parts[0]
            args = parts[1].strip(")").split(",")
            new_line = f"{command} {arg1}"
            for arg in args:
                new_line += f" {arg.strip()}"
            return new_line
        else:
            return line

    def do_quit(self, line):
        """Exit the program using quit()"""

        return True

    def do_EOF(self, line):
        """Exit the program using CTRL+D"""

        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""

        pass

    def do_create(self, line):
        """
        Create a new instance of a specific Class

        Usage:
            - create Class
            - Class.create()
        """

        arguments = parse_args(line)
        if not validate_args(arguments):
            return

        instance = classes[arguments[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id

        Usage:
            - show Class id
            - Class.show("id")
        """

        arguments = parse_args(line)
        if not validate_args(arguments, 3):
            return

        all_objects = storage.all()

        key = get_key(arguments[0], arguments[1])
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id

        Usage:
            - destroy Class id
            - Class.destroy("id")
        """

        arguments = parse_args(line)

        if not validate_args(arguments, 3):
            return

        all_objects = storage.all()
        key = get_key(arguments[0], arguments[1])

        if key not in all_objects:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name

        Usage:
            - all
            - all Class
            - Class.all()
        """

        arguments = parse_args(line)
        all_objects = storage.all()

        if len(arguments) == 0:
            print([str(str_rep) for str_rep in all_objects.values()])
        elif arguments[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_objects.values()
                   if type(obj).__name__ == arguments[0]])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute

        Usage:
            - update Class id attribute value
            - Class.update("id", "attribute", "value")
        """

        arguments = parse_args(line)
        if not validate_args(arguments, 5):
            return

        all_objects = storage.all()
        key = get_key(arguments[0], arguments[1])
        if key not in all_objects:
            print("** no instance found **")
            return

        setattr(all_objects[key], arguments[2], arguments[3])
        all_objects[key].save()

    def do_count(self, line):
        """
        Prints the current number of instances of a class

        Usage:
            - count Class
            - Class.count()
        """

        arguments = parse_args(line)
        if not validate_args(arguments):
            return

        all_objects = storage.all()
        number_of_instances = 0
        for obj in all_objects.values():
            if type(obj).__name__ == arguments[0]:
                number_of_instances += 1

        print(number_of_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
