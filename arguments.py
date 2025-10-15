from jsonSt import *
from exFunc import *
import copy
import time

store = "tasks.json"


def commandProcess(store, command, argument, updArgument):
    # Logic to deal with the arguments from the user input

    taskList = jsonDataRetrieval(
        store, command
    )  # It's a type: python dictionary, contrary to the name

    if command == "add":

        crtTime = time.strftime("%Y-%m-%d, %H:%M:%S")
        updTime = crtTime
        taskId = len(taskList) + 1
        newTask = {
            "description": argument,
            "status": "to-do",
            "createdAt": crtTime,
            "updatedAt": updTime,
        }
        taskList[taskId] = newTask

        print(f"Task with ID: {taskId} added succesfully!✅")

    elif command == "update":

        try:

            if not updArgument:
                print("Error: Update description is required!")
                sys.exit(1)

            taskId = argument  # This is just for reference
            taskList[taskId]["description"] = updArgument
            taskList[taskId]["updatedAt"] = time.strftime("%Y-%m-%d, %H:%M:%S")

            print(f"Updated task with ID: {taskId} to {updArgument}✒️")

        except KeyError as Error:
            print(
                f"Error: {type(Error).__name__} - Task with ID: {argument} is not found!"
            )
            sys.exit(1)

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")
            sys.exit(1)

    elif command == "delete":

        try:

            if not argument == "all":

                del taskList[argument]
                print(f"Task with ID: {argument} deleted!🚮")

            else:
                taskList.clear()
                print(f"All tasks deleted!🚮")

        except KeyError as Error:
            print(
                f"Error: {type(Error).__name__} - Task with ID: {argument} is not found!"
            )
            sys.exit(1)

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")
            sys.exit(1)

    elif command == "mark-done":
        try:

            statusCol = "status"
            updateTo = "done"
            taskList[argument][statusCol] = updateTo
            taskList[argument]["updatedAt"] = time.strftime("%Y-%m-%d, %H:%M:%S")

            print(f"Task with ID: {argument} updated to {updateTo}⌛")

        except KeyError as Error:
            print(
                f"Error: {type(Error).__name__} - Task with ID: {argument} is not found!"
            )
            sys.exit(1)

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")
            sys.exit(1)

    elif command == "mark-in-progress":

        try:

            statusCol = "status"
            updateTo = "in-progress"
            taskList[argument][statusCol] = updateTo
            taskList[argument]["updatedAt"] = time.strftime("%Y-%m-%d, %H:%M:%S")

            print(f"Task with ID: {argument} updated to {updateTo}⏳")

        except KeyError as Error:
            print(
                f"Error: {type(Error).__name__} - Task with ID: {argument} is not found!"
            )
            sys.exit(1)

        except Exception as Error:
            print(f"Error: {type(Error).__name__} - {Error}")

    elif command == "list":

        if argument == "all" or argument == "":
            checkForEmpty(taskList, tabulateData(taskList, "grid"))

        else:

            allTask = copy.deepcopy(taskList)
            toBeDel = []
            if argument == "in-progress" or argument == "done" or argument == "to-do":
                statusToDel = argument

            else:
                print("Error: Status not found!")
                sys.exit(1)

            for taskData in allTask.items():

                if (
                    not taskData[1]["status"] == statusToDel
                ):  # 1 is the value (description and the rest)

                    toBeDel.append(taskData[0])

            for keys in toBeDel:
                del allTask[keys]

            checkForEmpty(allTask, tabulateData(allTask, "grid"))

    else:
        print("Error: Invalid Argument!")
        sys.exit(1)

    dictDataToJson(store, taskList)
