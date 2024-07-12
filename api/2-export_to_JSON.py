#!/usr/bin/python3
""" Using REST api to return employee information
about his/her TODO list progress"""
import csv
import json
import requests
import sys


def todo_list_api(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    employee_name_r = requests.get(user_url)
    employee_name = employee_name_r.json().get('username')

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

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_total:
            writer.writerow([
                employee_id, employee_name,
                task.get('completed'), task.get('title')
            ])

    task = [{"task": task["title"], "completed":
            task["completed"], "username": employee_name}
            for task in todos_total]
    data = {str(employee_id): task}

    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    todo_list_api(int(sys.argv[1]))
