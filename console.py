#!/usr/bin/python3
""" created class  HBNBCommand """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = '(hbnb)'
    
    def	do_quit(self, line):
        """ exit program """
        return True

    def do_EOF(self, line):
        """ exit program """
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
