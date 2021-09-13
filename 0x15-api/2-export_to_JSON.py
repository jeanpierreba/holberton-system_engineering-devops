#!/usr/bin/python3
""" Exports file 0 result into json file """

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todos_user = {}
    tasks_list = []

    for task in todos:
        if task.get('userId') == int(user_id):
            taskDict = {"task": task.get("title"),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            tasks_list.append(taskDict)
    todos_user[user_id] = tasks_list

    filename = user_id + '.json'
    with open(filename, mode='w') as file:
        json.dump(todos_user, file)
