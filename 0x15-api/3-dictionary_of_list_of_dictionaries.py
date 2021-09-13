#!/usr/bin/python3
""" Dictionary of list of dictionaries """

import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    todos_list = {}

    for user in users:
        tasks_list = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                task_dict = {"username": user.get("username"),
                             "task": task.get("title"),
                             "completed": task.get("completed")}
                tasks_list.append(task_dict)
        todos_list[user.get("id")] = tasks_list

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        json.dump(todos_list, file)
