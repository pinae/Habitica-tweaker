from django.contrib import admin
from.models import Account
from.models import Todo, TodoChecklistItem, TodoId
from.models import Habit, HabitHistory, HabitId
from.models import Daily, DailyChecklistItem, DailyHistory, DailyId


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'sync_tag')


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'priority')


@admin.register(TodoChecklistItem)
class TodoChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'todo')


@admin.register(TodoId)
class TodoIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo')


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('text', 'priority')


@admin.register(HabitHistory)
class HabitHistoryAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'value')


@admin.register(HabitId)
class HabitIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'habit')


@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'priority')


@admin.register(DailyChecklistItem)
class DailyChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'daily')


@admin.register(DailyHistory)
class DailyHistoryAdmin(admin.ModelAdmin):
    list_display = ('daily', 'date', 'value')


@admin.register(DailyId)
class DailyIdAdmin(admin.ModelAdmin):
    list_display = ('id', 'daily')
