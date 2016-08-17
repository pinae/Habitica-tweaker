from django.http import HttpResponse
from .models import Account, Todo, Habit, Daily


def load_all_tasks(account):
    if not account.sync_tag:
        tasks = account.habitipy().get_tasks()
    else:
        tasks = account.habitipy().get_tasks_with_tag(account.sync_tag)
    for task in tasks:
        if task['type'] == 'todo':
            import json
            print(json.dumps(task, indent=4))
            todo = Todo(text=task['text'],
                        notes=task['notes'],
                        priority=task['priority'],
                        value=task['value'],
                        attribute=task['attribute'],
                        completed=task['completed'])
            print(task['id'])
            for checklist_item in task['checklist']:
                print(checklist_item['text'])
                print(checklist_item['completed'])
        elif task['type'] == 'habit':
            pass
        elif task['type'] == 'daily':
            pass
        """print(task['text'])
        print(task['notes'])
        print(task['type'])
        print(task['priority'])
        print(task['value'])
        print(task['attribute'])
        print(task['priority'])"""



def webhook(request):
    for account in Account.objects.all():
        load_all_tasks(account)
    return HttpResponse("OK")
