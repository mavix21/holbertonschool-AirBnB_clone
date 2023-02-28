#!/usr/bin/python3
""" This module defines the HBNBCommand interpreter """

import cmd
import json
import re
from utils.console_utils import validate_args, parse_args
from utils.common_utils import get_key
from utils.constants import re_cmd, re_inside_parenthesis
from models.__init__ import storage, classes


class HBNBCommand(cmd.Cmd):
    """ The entry point of the command interpreter """

    prompt = "(hbnb) "

    def precmd(self, line):
        """ Overrides the default precmd method """

        if line and re.match(re_cmd, line):
            parts = line.split(".")
            arg1 = parts[0]
            parts = parts[1].split("(")
            command = parts[0]
            new_line = f"{command} {arg1}"
            args = re.findall(re_inside_parenthesis, f"({parts[1]}")
            if len(args) == 0:
                return (new_line)

            try:
                args_list = json.loads(f"[{args[0]}]")
            except Exception as e:
                print(str(e))
                return ""

            for arg in args_list:
                if type(arg) is dict:
                    new_line += f" {json.dumps(arg)}"
                else:
                    new_line += f" \"{arg}\""
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
            - Class.update("id", dictionary)
        """

        arguments = parse_args(line)
        if not validate_args(arguments, 3):
            return

        all_objects = storage.all()
        key = get_key(arguments[0], arguments[1])
        if key not in all_objects:
            print("** no instance found **")
            return

        if re.match(r"(\{.*\})", arguments[2]):
            try:
                attr_dict = json.loads(arguments[2])
            except Exception as e:
                if "value" in str(e):
                    print("** value missing **")
                elif "name" in str(e):
                    print("** value missing **")
                else:
                    print(e)
                return
        elif validate_args(arguments, 5):
            if type(arguments[3]) is str:
                if arguments[3].isdigit():
                    arguments[3] = int(arguments[3])
                else:
                    try:
                        arguments[3] = float(arguments[3])
                    except ValueError:
                        pass

            attr_dict = {f"{arguments[2]}": arguments[3]}
        else:
            return

        for i in attr_dict:
            if i in ["id", "created_at", "updated_at"]:
                print(f"Cannot update {key} attribute")
                return

        obj_to_upd = all_objects[key]
        obj_to_upd.__dict__.update(**attr_dict)
        obj_to_upd.save()

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
