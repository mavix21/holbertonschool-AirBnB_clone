#!/usr/bin/python3
""" created class  HBNBCommand """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """ Exit program """
        return True

    def do_EOF(self, line):
        """ Exit program """
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        print("")

    def do_create(self, line):
        """Create a new instance of BaseModel"""
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
        """Deletes an instance based on the class name and id"""

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
        """Prints all string representation of all instances based or not on
        the class name."""
        argument = line.split()
        all_storage = storage.all()
        if len(argument) == 0:
            print(all_storage)
        else:
            if argument[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(all_storage)


<<<<<<< HEAD
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        argument = line.split()
        all_object = storage.all()
        key = "{}.{}".format(argument[0], argument[1])
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif key not in all_object:
            print("** no instance found **")
        elif len(argument) == 2:
            print("** attribute name missing **")
        elif len(argument) == 3:
            print("** value missing **")

=======
>>>>>>> aa02a915e6ead57397c3d6d555900fd775c9e6e6
if __name__ == '__main__':
    HBNBCommand().cmdloop()
