#!/usr/bin/python3
""" This module defines the HBNBCommand interpreter """

import cmd
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
    intro = "\o/  Welcome to HBNB command line  \o/"
    prompt = "(hbnb) "

    @staticmethod
    def parse(line):
        """ Parse the command line into argumentss """
        args = []
        quote_mode = False
        arg_start = 0

        for i, c in enumerate(line):
            if c == '"':
                quote_mode = not quote_mode
            elif not quote_mode and c.isspace():
                if arg_start < i:
                    args.append(line[arg_start:i])
                arg_start = i + 1

        if arg_start < len(line):
            args.append(line[arg_start:])

        return [arg.strip('"') for arg in args]

    @staticmethod
    def validate_args(args, number_of_validations=2):
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1 and number_of_validations >= 3:
            print("** instance id missing **")
            return False

        if len(args) == 2 and number_of_validations >= 4:
            print("** attribute name missing **")
            return False

        if len(args) == 3 and number_of_validations >= 5:
            print("** value missing **")
            return False

        return True

    @staticmethod
    def get_key(class_name, id):
        return f"{class_name}.{id}"

    def do_quit(self, line):
        """ Exit the program """

        return True

    def do_EOF(self, line):
        """ Exit the program """

        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line """

        pass

    def do_create(self, line):
        """ Create a new instance of BaseModel """

        arguments = self.parse(line)
        if not self.validate_args(arguments):
            return

        instance = classes[arguments[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """

        arguments = self.parse(line)
        if not self.validate_args(arguments, 3):
            return

        all_objects = storage.all()

        key = self.get_key(arguments[0], arguments[1])
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """

        arguments = self.parse(line)

        if not self.validate_args(arguments, 3):
            return

        all_objects = storage.all()
        key = self.get_key(arguments[0], arguments[1])

        if key not in all_objects:
            print("** no instance found **")
        else:
            del all_objects[key]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name
        """

        arguments = self.parse(line)
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
        """

        arguments = self.parse(line)
        if self.validate_args(arguments, 5):
            return

        all_objects = storage.all()

        key = self.get_key(arguments[0], arguments[1])
        if key not in all_objects:
            print("** no instance found **")
            return

        setattr(all_objects[key], arguments[2], arguments[3])
        all_objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
