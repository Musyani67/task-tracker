from tabulate import tabulate  # type: ignore
import sys


def tabulateData(taskList, tablefmt):
    # Takes the data in (dictionary) presents it into a table (Specific though, needs generalization)

    try:

        headers = ["ID", "Description", "Status", "Created At", "Updated At"]
        rows = []
        for taskId, taskData in taskList.items():
            rows.append(
                [
                    taskId,
                    taskData["description"],
                    taskData["status"],
                    taskData["createdAt"],
                    taskData["updatedAt"],
                ]
            )

        table = tabulate(rows, headers, tablefmt=tablefmt)

        return table

    except Exception as Error:
        print(f"Error: {type(Error).__name__} - {Error}")
        sys.exit(1)


def checkForEmpty(anyList, message):

    if len(anyList) == 0:
        print("No specified tasks!")

    else:
        print(message)
