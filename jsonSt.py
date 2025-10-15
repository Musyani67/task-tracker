import json
import os
import sys


def jsonCreate(store):
    # Creates the JSON file and pushes an empty dictionary into it.

    if not os.path.exists(store):
        try:
            with open(store, "x"):
                pass
            #   print("File created✅")

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")
            sys.exit(1)

    if os.stat(store).st_size == 0:

        try:
            with open(store, "w") as file:

                tasks = {}
                json.dump(tasks, file, indent=4)
                # print("File saved in JSON✅")

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")
            sys.exit(1)


def jsonDataRetrieval(store, description):
    # Gets the data from the JSON file (storage)

    try:
        with open(store, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("Error: JSON file not found.")
        sys.exit(1)

    except Exception as Error:
        print(f"Error: {type(Error).__name__} - {Error}")
        sys.exit(1)

    return data


def dictDataToJson(store, data):  # The data is the python dictionary
    # Converts the list to JSON for storage

    try:
        with open(store, "w") as file:

            json.dump(data, file, indent=4)

    except Exception as Error:
        print(f"Error: {type(Error).__name__} - {Error}")
