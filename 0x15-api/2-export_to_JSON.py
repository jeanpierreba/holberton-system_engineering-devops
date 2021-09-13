#!/usr/bin/python3
""" Exports file 0 result into json file """

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    todos_user = {}
    tasks_list = []

    for task in todos:
        if task.get("userId") == int(user_id):
            task_dict = {"task": task.get("title"),
                         "completed": task.get('completed'),
                         "username": user.json().get("username")}
            tasks_list.append(task_dict)
    todos_user[user_id] = tasks_list

    file_name = user_id + '.json'
    with open(file_name, 'w') as file:
        json.dump(todos_user, file)
