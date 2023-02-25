#!/usr/bin/python3
""" This module defines the HBNBCommand interpreter """

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ The entry point of the command interpreter """
    prompt = "(hbnb) "

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

        argument = line.split()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """

        argument = line.split()
        call_storage = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argument[0], argument[1])
            if key in call_storage:
                print(call_storage[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """

        argument = line.split()
        call_storage = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argument[0], argument[1])
            if key not in call_storage:
                print("** no instance found **")
            else:
                del call_storage[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on
        the class name
        """

        argument = line.split()
        all_storage = storage.all()
        if len(argument) == 0:
            print(all_storage)
        else:
            if argument[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(all_storage)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """

        argument = line.split()
        all_objects = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
            return
        elif argument[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif len(argument) == 1:
            print("** instance id missing **")
            return
        elif len(argument) == 2:
            print("** attribute name missing **")
            return
        elif len(argument) == 3:
            print("** value missing **")
            return

        key = "{}.{}".format(argument[0], argument[1])
        if key not in all_objects:
            print("** no instance found **")
            return

        setattr(all_objects[key], argument[2], argument[3])
        all_objects[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
