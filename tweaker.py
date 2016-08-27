#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import habitipy
import requests
try:
    from private_settings import accounts
except ImportError:
    accounts = []


if __name__ == "__main__":
    print("Hallo Welt.")
    """headers = {'x-api-user': USER_ID, 'x-api-key': API_KEY}
    response = requests.get('https://habitica.com/api/v3/groups/party', headers=headers)
    group_id = response.json()['data']['id']
    print(group_id)
    response = requests.get('https://habitica.com/api/v3/user', headers=headers)
    last_cron = response.json()['data']['lastCron']  # "2016-08-16T06:37:22.388Z"
    mana = response.json()['data']['stats']['mp']
    health = response.json()['data']['stats']['hp']
    print(mana)
    print(health)"""
    import json
    #print(json.dumps(response.json(), sort_keys=True, indent=4))
    main_account = habitipy.HabiticaAccount(accounts[0][0]['USER_ID'], accounts[0][0]['API_KEY'])
    #print(json.dumps(main_account.get_tasks_with_tag(main_account.get_tag_id("Arbeit")), sort_keys=True, indent=4))
    #print(json.dumps(main_account.get_task("497c993a-1f41-4f20-88fd-99620a7b9215"), sort_keys=True, indent=4))
    print("--------------------------------------")
    print(json.dumps(main_account.get_task("d90b363e-8529-4d65-8dc3-29ad9922ed8d"), indent=4))
    #print(main_account.update_todo("e28caace-9e45-45ab-bb98-fe6c0a511220", notes=""))
    #print(json.dumps(main_account.get_current_quest(), sort_keys=True, indent=4))
    work_account = habitipy.HabiticaAccount(accounts[0][1]['USER_ID'], accounts[0][1]['API_KEY'])
    #print(json.dumps(work_account.get_user_data(), sort_keys=True, indent=4))
    #print(json.dumps(work_account.create_todo("ABC"), sort_keys=True, indent=4))
    #print(json.dumps(main_account.get_current_quest(), sort_keys=True, indent=4))
    #print(json.dumps(main_account.get_stats(), indent=4))
    #print(json.dumps(work_account.get_tasks(), sort_keys=True, indent=4))
    #print(not work_account.get_current_quest()['key'])
    """print(work_account.create_daily("test 1", repeat_days={'m': 0, 't': 1, 'w': 0, 'th': 1, 'f': 0, 's': 0, 'su': 0},
                                    priority=0.1))
    print(work_account.create_daily("test 2", every_x=3, priority=1.5))
    print(work_account.create_habit("some habit", priority=2))
    print(work_account.create_habit("bad habit", good=False, bad=True))
    print(work_account.create_todo("some todo", priority=1.5))"""

