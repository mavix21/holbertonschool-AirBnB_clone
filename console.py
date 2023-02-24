#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = '(hbnb)'
    
    def	do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        print("")

if __name__ == '__main__':
    HBNBCommand().cmdloop()    
