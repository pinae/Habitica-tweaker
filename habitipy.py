#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import requests, json


class HabiticaAccount:
    def __init__(self, user_id, api_key):
        self.headers = {'x-api-user': user_id, 'x-api-key': api_key}

    def get_tags(self):
        response = requests.get('https://habitica.com/api/v3/tags', headers=self.headers)
        return response.json()['data']

    def get_tag_id(self, tag_name):
        for tag in self.get_tags():
            if tag['name'] == tag_name:
                return tag['id']

    def get_tasks(self):
        response = requests.get('https://habitica.com/api/v3/tasks/user', headers=self.headers)
        return response.json()['data']

    def get_tasks_with_tag(self, tag_id):
        task_list = []
        for task in self.get_tasks():
            if tag_id in task['tags']:
                task_list.append(task)
        return task_list

    def create_daily(self,
                     text,
                     repeat_days=False,
                     every_x=False,
                     checklist=False,
                     notes='',
                     priority=1,
                     attribute='str',
                     value=1.947771358054911):
        if priority not in [0.1, 1, 1.5, 2]:
            priority = 1
        new_task = {
            'text': text,
            'notes': notes,
            'priority': priority,
            'attribute': attribute,
            'value': value,
            'type': 'daily'
        }
        if checklist:
            new_task['checklist'] = checklist
        if repeat_days:
            new_task['everyX'] = 1
            new_task['repeat'] = repeat_days
            new_task['frequency'] = 'weekly'
        elif every_x:
            new_task['everyX'] = every_x
            new_task['repeat'] = {'m': True, 't': True, 'w': True, 'th': True, 'f': True,
                                  's': True, 'su': True}
            new_task['frequency'] = 'daily'
        response = requests.post('https://habitica.com/api/v3/tasks/user',
                                 json=[new_task],
                                 headers=self.headers)
        if response.status_code != 201:
            print(response.json())
        return response.status_code == 201

    def create_habit(self,
                     text,
                     good=True,
                     bad=False,
                     notes='',
                     priority=1,
                     attribute='str',
                     value=1.947771358054911):
        if not good and not bad:
            good = True
        if priority not in [0.1, 1, 1.5, 2]:
            priority = 1
        new_task = {
            'text': text,
            'up': good,
            'down': bad,
            'notes': notes,
            'priority': priority,
            'attribute': attribute,
            'value': value,
            'type': 'habit'
        }
        response = requests.post('https://habitica.com/api/v3/tasks/user',
                                 json=[new_task],
                                 headers=self.headers)
        if response.status_code != 201:
            print(response.json())
        return response.status_code == 201

    def create_todo(self,
                    text,
                    notes='',
                    priority=1,
                    checklist=False,
                    attribute='str',
                    value=False,
                    completed=False,
                    updated_at=None):
        if priority not in [0.1, 1, 1.5, 2]:
            priority = 1
        new_task = {
            'text': text,
            'notes': notes,
            'priority': priority,
            'attribute': attribute,
            'completed': completed,
            'type': 'todo'
        }
        if checklist:
            new_task['checklist'] = checklist
        if value:
            new_task['value'] = value
        if updated_at is not None:
            new_task['updatedAt'] = updated_at
        response = requests.post('https://habitica.com/api/v3/tasks/user',
                                 json=[new_task],
                                 headers=self.headers)
        if response.status_code != 201:
            print(response.json())
        return response.status_code == 201

    def get_todo(self, task_id):
        response = requests.get('https://habitica.com/api/v3/tasks/' + task_id, headers=self.headers)
        return response.json()['data']

    def update_todo(self,
                    task_id,
                    text=None,
                    notes=None,
                    priority=None,
                    checklist=None,
                    attribute=None,
                    value=None,
                    completed=None,
                    updated_at=None):
        todo = self.get_todo(task_id)
        if todo['type'] != 'todo':
            return False
        if text is not None:
            todo['text'] = text
        if notes is not None:
            todo['notes'] = notes
        if priority is not None and priority in [0.1, 1, 1.5, 2]:
            todo['priority'] = priority
        if checklist is not None:
            todo['checklist'] = checklist
        if attribute is not None:
            todo['attribute'] = attribute
        if value is not None:
            todo['value'] = value
        if completed is not None:
            todo['completed'] = completed
        if updated_at is not None:
            todo['updatedAt'] = updated_at
        response = requests.put('https://habitica.com/api/v3/tasks/' + task_id,
                                json=todo,
                                headers=self.headers)
        if response.status_code != 200:
            print(response.json())
        return response.status_code == 200

    def get_stats(self):
        response = requests.get('https://habitica.com/api/v3/user', headers=self.headers)
        return response.json()['data']['stats']

    def get_user_data(self):
        response = requests.get('https://habitica.com/api/v3/user', headers=self.headers)
        return response.json()['data']

    def get_current_quest(self):
        response = requests.get('https://habitica.com/api/v3/user', headers=self.headers)
        return response.json()['data']['party']['quest']

    def get_group_id(self):
        response = requests.get('https://habitica.com/api/v3/groups/party', headers=self.headers)
        return response.json()['data']['id']

    def post_message_to_party(self, message):
        response = requests.post('https://habitica.com/api/v3/groups/party/chat',
                                 json={"message": message},
                                 headers=self.headers)
        return response.status_code == 200
