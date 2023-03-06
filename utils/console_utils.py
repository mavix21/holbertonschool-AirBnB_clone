#!/usr/bin/python3
""" This module defines utility functions for the console """

from models.__init__ import classes


def parse_args(line):
    """ Parse the command line into arguments """

    args = []
    quote_mode = False
    brace_mode = False
    brace_level = 0
    arg_start = 0

    for i, c in enumerate(line):
        if c == '"':
            if brace_mode:
                continue
            quote_mode = not quote_mode
        elif c == '{':
            if not quote_mode:
                brace_mode = True
            brace_level += 1
        elif c == '}':
            if not quote_mode:
                brace_level -= 1

            if brace_level == 0:
                brace_mode = False
        elif not quote_mode and not brace_mode and c.isspace():
            if arg_start < i:
                args.append(line[arg_start:i])
            arg_start = i + 1

    if arg_start < len(line):
        args.append(line[arg_start:])

    args = [arg.strip('"') for arg in args]
    final_args = []
    for arg in args:
        if '{' in arg and '}' in arg:
            start = arg.find('{')
            end = arg.rfind('}')
            final_args.extend(arg[:start].split())
            final_args.append(arg[start:end+1])
            final_args.extend(arg[end+1:].split())
        else:
            final_args.append(arg)

    return final_args


def validate_args(args, number_of_validations=2):
    """ Validate arguments passed to the available commands on the console """
    if len(args) == 0:
        print("** class name missing **")
        return False

    if args[0] not in classes:
        print("** class doesn't exist **")
        return False

    if number_of_validations >= 3 and len(args) == 1:
        print("** instance id missing **")
        return False

    if number_of_validations >= 4 and len(args) == 2:
        print("** attribute name missing **")
        return False

    if number_of_validations >= 5 and len(args) == 3:
        print("** value missing **")
        return False

    return True
