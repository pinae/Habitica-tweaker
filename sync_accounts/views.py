from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Account
from .models import Todo, TodoId, TodoChecklistItem
from .models import Habit, HabitHistory, HabitId
from .models import Daily, DailyId, DailyChecklistItem, DailyHistory
import dateutil.parser as time_parser
import json


def update_todo(todo, task_dict):
    todo.text = task_dict['text']
    todo.notes = task_dict['notes']
    todo.priority = task_dict['priority']
    todo.value = task_dict['value']
    todo.attribute = task_dict['attribute']
    todo.completed = task_dict['completed']
    todo.updated_at = time_parser.parse(task_dict['updatedAt'])
    todo.checklist.all().delete()
    todo.save()
    for item in task_dict['checklist']:
        new_item = TodoChecklistItem(todo=todo, text=item['text'], completed=item['completed'])
        new_item.save()


def update_habit(habit, task_dict):
    habit.text = task_dict['text']
    habit.notes = task_dict['notes']
    habit.good = task_dict['up']
    habit.bad = task_dict['down']
    habit.priority = task_dict['priority']
    habit.value = task_dict['value']
    habit.attribute = task_dict['attribute']
    habit.updated_at = time_parser.parse(task_dict['updatedAt'])
    habit.history.all().delete()
    habit.save()
    for item in task_dict['history']:
        new_history_item = HabitHistory(habit=habit, date=item['date'], value=item['value'])
        new_history_item.save()


def update_daily(daily, task_dict):
    daily.text = task_dict['text']
    daily.notes = task_dict['notes']
    daily.priority = task_dict['priority']
    daily.value = task_dict['value']
    daily.attribute = task_dict['attribute']
    daily.everyX = task_dict['everyX'],
    daily.repeat_days = json.dumps(task_dict['repeat'])
    daily.updated_at = time_parser.parse(task_dict['updatedAt'])
    daily.checklist.all().delete()
    daily.history.all().delete()
    daily.save()
    for item in task_dict['checklist']:
        new_item = DailyChecklistItem(daily=daily, text=item['text'], completed=item['completed'])
        new_item.save()
    for item in task_dict['history']:
        new_history_item = DailyHistory(daily=daily, date=item['date'], value=item['value'])
        new_history_item.save()


def load_all_tasks(account):
    if not account.sync_tag:
        tasks = account.habitipy().get_tasks()
    else:
        tasks = account.habitipy().get_tasks_with_tag(
            account.habitipy().get_tag_id(account.sync_tag))
    for task in tasks:
        if task['type'] == 'todo':
            try:
                todo_id = TodoId.objects.get(id=task['id'], account=account)
                todo = todo_id.todo
                if todo.updated_at < time_parser.parse(task['updatedAt']):
                    update_todo(todo, task)
            except TodoId.DoesNotExist:
                try:
                    todo = Todo.objects.get(text=task['text'])
                    new_id = TodoId(todo=todo, id=task['id'], account=account)
                    new_id.save()
                    if todo.updated_at < time_parser.parse(task['updatedAt']):
                        update_todo(todo, task)
                except Todo.DoesNotExist:
                    todo = Todo(text=task['text'],
                                notes=task['notes'],
                                priority=task['priority'],
                                value=task['value'],
                                attribute=task['attribute'],
                                completed=task['completed'],
                                updated_at=time_parser.parse(task['updatedAt']))
                    todo.save()
                    new_id = TodoId(todo=todo, id=task['id'], account=account)
                    new_id.save()
                    for item in task['checklist']:
                        new_item = TodoChecklistItem(todo=todo, text=item['text'], completed=item['completed'])
                        new_item.save()
        elif task['type'] == 'habit':
            try:
                habit_id = HabitId.objects.get(id=task['id'], account=account)
                habit = habit_id.habit
                if habit.updated_at < time_parser.parse(task['updatedAt']):
                    update_habit(habit, task)
            except HabitId.DoesNotExist:
                try:
                    habit = Habit.objects.get(text=task['text'])
                    new_id = HabitId(habit=habit, id=task['id'], account=account)
                    new_id.save()
                    if habit.updated_at < time_parser.parse(task['updatedAt']):
                        update_habit(habit, task)
                except Habit.DoesNotExist:
                    habit = Habit(text=task['text'],
                                  notes=task['notes'],
                                  good=task['up'],
                                  bad=task['down'],
                                  priority=task['priority'],
                                  value=task['value'],
                                  attribute=task['attribute'],
                                  updated_at=time_parser.parse(task['updatedAt']))
                    habit.save()
                    new_id = HabitId(habit=habit, id=task['id'], account=account)
                    new_id.save()
                    for item in task['history']:
                        new_history_item = HabitHistory(habit=habit,
                                                        date=item['date'],
                                                        value=item['value'])
                        new_history_item.save()
        elif task['type'] == 'daily':
            try:
                daily = DailyId.objects.get(id=task['id'], account=account).daily
                if daily.updated_at < time_parser.parse(task['updatedAt']):
                    update_daily(daily, task)
            except DailyId.DoesNotExist:
                try:
                    daily = Daily.objects.get(text=task['text'])
                    new_id = DailyId(daily=daily, id=task['id'], account=account)
                    new_id.save()
                    if daily.updated_at < time_parser.parse(task['updatedAt']):
                        update_daily(daily, task)
                except Daily.DoesNotExist:
                    daily = Daily(text=task['text'],
                                  notes=task['notes'],
                                  priority=task['priority'],
                                  value=task['value'],
                                  attribute=task['attribute'],
                                  completed=task['completed'],
                                  everyX=task['everyX'],
                                  repeat_days=json.dumps(task['repeat']),
                                  updated_at=time_parser.parse(task['updatedAt']))
                    daily.save()
                    new_id = DailyId(daily=daily, id=task['id'], account=account)
                    new_id.save()
                    for item in task['checklist']:
                        new_item = DailyChecklistItem(daily=daily, text=item['text'], completed=item['completed'])
                        new_item.save()
                    for item in task['history']:
                        new_history_item = DailyHistory(daily=daily, date=item['date'], value=item['value'])
                        new_history_item.save()


def update_all_tasks(account):
    for todo in Todo.objects.all():
        checklist = []
        for item in todo.checklist.all():
            checklist.append({
                'text': item.text,
                'completed': item.completed
            })
        if len(todo.ids.filter(account=account).all()) > 0:
            task_id = todo.ids.filter(account=account).all()[0].id
            account.habitipy().update_todo(
                task_id,
                text=todo.text,
                notes=todo.notes,
                priority=todo.priority,
                value=todo.value,
                attribute=todo.attribute,
                completed=todo.completed,
                updated_at=todo.updated_at.isoformat(),
                checklist=checklist
            )
        else:
            account.habitipy().create_todo(
                text=todo.text,
                notes=todo.notes,
                priority=todo.priority,
                value=todo.value,
                attribute=todo.attribute,
                completed=todo.completed,
                updated_at=todo.updated_at.isoformat(),
                checklist=checklist)


def webhook(request):
    for user in User.objects.all():
        if user.accounts.count() >= 2:
            accounts = user.accounts.all()
            for account in accounts:
                load_all_tasks(account)
            for account in accounts:
                update_all_tasks(account)
    return HttpResponse("OK")
