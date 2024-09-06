#!/usr/bin/python3
"""a python script that uses REST API to provide  a given employee
by their id"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    user_data = res.json()
    print("Employee {} is done with tasks"
          .format(user_data.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
