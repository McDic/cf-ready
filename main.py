import typing
from argparse import ArgumentParser, HelpFormatter


def get_parser() -> ArgumentParser:
    """
    Get main program parser.
    """

    PROGRAM_NAME: typing.Final[str] = "CP-Ready"

    def help_formatter(prog: str) -> HelpFormatter:
        return HelpFormatter(prog, width=120)

    main_parser = ArgumentParser(
        prog=PROGRAM_NAME,
        description=f"Main python program for {PROGRAM_NAME}",
        formatter_class=help_formatter,
    )
    main_subparsers = main_parser.add_subparsers()

    contest_parser = main_subparsers.add_parser(
        "contest", help="Manage contests", formatter_class=help_formatter
    )
    contest_subparsers = contest_parser.add_subparsers()

    contest_init_parser = contest_subparsers.add_parser(
        "init",
        help="Init new contest repository",
        description="""
        dd
        """,
        formatter_class=help_formatter,
    )
    contest_init_parser.add_argument(
        "--id",
        type=int,
        help="""
            Give an exact contest ID.
            1874 for "Codeforces Round 901 (Div. 1)" for example.
            If the given ID cannot be found, then the program will fail.
        """,
    )
    contest_init_parser.add_argument(
        "--name",
        type=str,
        help="""
            Give contest name. This will find the contest that matches
            the entered name as subsequence, case insensitive.
            If multiple contests are matched or you cannot register to
            the target contest, then the program will fail.
            "901d1" for "Codeforces Round 901 (Div. 1)" for example.
        """,
    )
    contest_init_parser.add_argument(
        "--include-gym",
        action="store_true",
        help="Include gym contests to search. Performance may be slower.",
    )

    return main_parser


def main():
    namespace = get_parser().parse_args()
    print(namespace)


if __name__ == "__main__":
    main()
