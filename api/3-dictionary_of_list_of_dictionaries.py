#!/usr/bin/python3
""" Using REST api to return employee information
about his/her TODO list progress"""
import csv
import json
import requests
import sys


def todo_list_api():
    """ Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = f"https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    """Get all users"""
    employee_name = requests.get(user_url).json()

    all_data = {}

    for user in employee_name:
        user_id = user['id']
        username = user['username']
        param = {'userId': user_id}
        todos_re = requests.get(todo_url, params=param).json()
        all_data[user_id] = [{
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        } for task in todos_re]

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_data, json_file)

if __name__ == "__main__":
    todo_list_api()
