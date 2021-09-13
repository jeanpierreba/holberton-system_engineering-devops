#!/usr/bin/python3
""" Exports file 0 result into a csv file """

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    fileName = user_id + '.csv'

    with open(fileName, 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get("userId") == int(user_id):
                writer.writerow([user_id, name, str(task.get("completed")),
                                task.get("title")])
