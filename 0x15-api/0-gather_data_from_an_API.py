#!/usr/bin/python3
""" Python script that uses REST API to returns information about a given
employee's TODO list progress """
import requests
from sys import argv

def get_todo_list():
    """
    Gets the todo lists of a given employee
    """
    employee_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee = response.json()
    name = employee['name']
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()
    completed = [todo for todo in todos if todo['completed']]
    print(f'Employee {name} is done with tasks({len(completed)}/{len(todos)}):')
    for todo in completed:
        print(f'\t{todo["title"]}')

if __name__ == '__main__':
    get_todo_list()
