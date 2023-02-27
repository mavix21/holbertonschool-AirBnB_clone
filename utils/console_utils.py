#!/usr/bin/python3
""" This module defines utility functions for the console """

from models.__init__ import classes


def parse_args(line):
    """ Parse the command line into arguments """

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


def validate_args(args, number_of_validations=2):
    if len(args) == 0:
        print("** class name missing **")
        return False

    if args[0] not in classes:
        print("** class doesn't exist **")
        return False

    if number_of_validations >= 3 and len(args) == 1:
        print("** instance id missing **")
        return False

    if number_of_validations >= 4 and len(args) == 1:
        print("** attribute name missing **")
        return False

    if number_of_validations >= 5 and len(args) == 1:
        print("** value missing **")
        return False

    return True
