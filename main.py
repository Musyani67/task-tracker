import argparse
from jsonSt import jsonCreate
from arguments import *
import sys


def main():

    store = "tasks.json"
    parser = argparse.ArgumentParser(
        prog="task-tracker",
        description="A program to track your tasks. You can add, update, or delete your tasks.",
    )
    parser.add_argument(
        "command",
        help="What to execute (add, update, list, mark-done, mark-in-progress or delete)",
    )  # This is the action to be done
    parser.add_argument(
        "details", type=str, help="The object the action is done to"
    )  # The object the action is done to
    parser.add_argument(
        "update_info",
        type=str,
        help="The information to replace with the exisiting.",
        nargs="?",
    )

    args = parser.parse_args()

    jsonCreate(store)

    commandProcess(store, args.command, args.details, args.update_info)


if __name__ == "__main__":
    main()
