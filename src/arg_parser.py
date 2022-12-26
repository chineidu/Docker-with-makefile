from argparse import ArgumentParser


def arg_parser_1() -> str:
    """ArgParser with verbosity as an input (integer)"""
    parser = ArgumentParser()
    parser.add_argument("square", help="calculate the `square` of an integer", type=int)
    parser.add_argument(
        "-v", "--verbose", help="increase the verbosity", type=int, choices=[0, 1, 2]
    )
    args = parser.parse_args()
    result = args.square**2

    if args.verbose == 1:
        print(f"square of {args.square} = {result}")
    elif args.verbose == 2:
        print(f"the square of {args.square} equals {result}\n")
    else:
        print(result)


def arg_parser_2() -> str:
    """ArgParser with verbosity as an input (count)"""
    parser = ArgumentParser()
    parser.add_argument("square", help="calculate the `square` of an integer", type=int)
    parser.add_argument(
        "-v", "--verbose", help="increase the verbosity", action="count", default=0
    )
    args = parser.parse_args()
    result = args.square**2

    if args.verbose == 1:
        print(f"square of {args.square} = {result}")
    elif args.verbose >= 2:
        print(f"the square of {args.square} equals {result}\n")
    else:
        print(result)


def arg_parser_3():
    """ArgParser with three arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "--name", "-n", type=str, help="The name of the data scientist / engineer"
    )
    parser.add_argument(
        "--role", "-r", type=str, help="The role of the data scientist / engineer"
    )
    parser.add_argument(
        "--level", "-l", type=str, help="The level of the data scientist / engineer"
    )
    parser.add_argument(
        "--verbose", "-v", action="count", help="Increase the verbosity", default=0
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="The name of the data scientist / engineer",
    )

    args = parser.parse_args()
    name, role, level = args.name, args.role, args.level

    if args.verbose >= 2:
        print(
            f"Hello {name!r}, you're a/an {role!r} and your current level is {level!r}\n"
        )
    elif args.verbose == 1:
        print(f"name={name}, role={role}, level={level}")
    elif args.quiet or args.verbose == 0:
        print(name, role, level)


# Call Function
arg_parser_3()
