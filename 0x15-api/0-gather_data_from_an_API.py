#!/usr/bin/python3
""" for a given employee ID, returns information
about his/her TODO list progress """

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    number_of_tasks = 0
    done_tasks = 0

    for task in todos.json():
        if task.get("userId") == int(user_id):
            number_of_tasks += 1
            if task.get("completed"):
                done_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_tasks, number_of_tasks))

    print('\n'.join(["\t " + task.get("title") for task in todos.json()
          if task.get("userId") == int(user_id) and task.get("completed")]))
