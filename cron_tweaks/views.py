#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


def fuck_my_life(account, accounts_hp=None):
    if accounts_hp is not None and account in accounts_hp:
        current_hp = accounts_hp[account]
    else:
        current_hp = account.habitipy().get_stats()['hp']
    tasks = account.habitipy().get_tasks()
    for task in tasks:
        if task['text'] == "Fuck my life!":
            if task['notes'].split(':')[0] == "relaxed":
                if not account.habitipy().get_current_quest()['key'] is None:
                    break
            try:
                target = int(task['notes'].split(':')[-1])
                if current_hp > target:
                    account.habitipy().set_hp(target)
                    break
            except ValueError:
                break


def bad_habit_fuck_me(account):
    if account.habitipy().get_current_quest()['key'] is None:
        tasks = account.habitipy().get_tasks()
        for task in tasks:
            if task['text'] == "Fuck my life!":
                try:
                    target = int(task['notes'])
                    while account.habitipy().get_stats()['hp'] > target:
                        account.habitipy().score_task(task['id'], down=True)
                    break
                except ValueError:
                    break
