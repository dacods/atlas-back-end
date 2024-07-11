#!/usr/bin/python3
""" Using REST api to return employee information
about his/her TODO list progress"""
import requests
import sys


def todo_list_api(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    employee_name_r = requests.get(user_url)
    employee_name = employee_name_r.json().get('name')

    params = {'userId': employee_id}
    todos_total_r = requests.get(todo_url, params=params)
    todos_total = todos_total_r.json()
    finished_task = [todo for todo in todos_total if todo['completed']]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(finished_task)}/{len(todos_total)}):"
    )
    for task in finished_task:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    todo_list_api(int(sys.argv[1]))
