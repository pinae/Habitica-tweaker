#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals


def fuck_my_life(account):
    if not account.habitipy().get_current_quest()['key']:
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
