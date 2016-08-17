from django.db import models
from habitipy import HabiticaAccount


class Account(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    api_key = models.CharField(max_length=50)
    cron_time = models.TimeField(blank=True)
    sync_tag = models.CharField(max_length=50, default='', blank=True)

    def is_main(self):
        return self.sync_tag == ''

    def habitipy(self):
        return HabiticaAccount(self.user_id, self.api_key)

    def __str__(self):
        s = self.user_id + 'Sync: '
        if self.is_main():
            s += 'all'
        else:
            s += self.sync_tag
        return s


class Todo(models.Model):
    text = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    priority = models.FloatField(default=1)
    value = models.FloatField(default=1.0)
    attribute = models.CharField(max_length=3, default='str')
    completed = models.BooleanField(default=False)

    def __str__(self):
        s = 'Todo: ' + str(self.text) + ' (' + str(self.priority) + ')'
        if self.completed:
            return 'Completed: ' + s
        else:
            return s


class TodoChecklistItem(models.Model):
    todo = models.ForeignKey(Todo, related_name='checklist')
    text = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        if self.completed:
            return 'Finished: ' + str(self.text)
        else:
            return str(self.text)


class TodoId(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    todo = models.ForeignKey(Todo, related_name='ids')
    account = models.ForeignKey(Account, related_name='todo_ids')

    def __str__(self):
        return self.id


class Habit(models.Model):
    text = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    good = models.BooleanField(default=True)
    bad = models.BooleanField(default=False)
    priority = models.FloatField(default=1)
    value = models.FloatField(default=1.0)
    attribute = models.CharField(max_length=3, default='str')

    def __str__(self):
        return 'Habit: ' + str(self.text) + ' (' + str(self.priority) + ')'


class HabitId(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    habit = models.ForeignKey(Habit, related_name='ids')
    account = models.ForeignKey(Account, related_name='habit_ids')

    def __str__(self):
        return self.id


class Daily(models.Model):
    text = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    priority = models.FloatField(default=1)
    value = models.FloatField(default=1.0)
    attribute = models.CharField(max_length=3, default='str')
    repeat_days = models.CharField(max_length=50, blank=True)
    everyX = models.IntegerField(default=1)


class DailyChecklistItem(models.Model):
    daily = models.ForeignKey(Daily, related_name='checklist')
    text = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class DailyId(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    daily = models.ForeignKey(Daily, related_name='ids')
    account = models.ForeignKey(Account, related_name='daily_ids')

    def __str__(self):
        return self.id
