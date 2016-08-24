#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from django.core.management.base import BaseCommand
from sync_accounts.models import Account
from ...views import fuck_my_life


class Command(BaseCommand):
    help = 'Check all Habitica-accounts for "Fuck my life!" habits and score them ' + \
           'till the hp are below the number in the notes.'

    def handle(self, *args, **options):
        accounts_hp = {}
        for account in Account.objects.all():
            accounts_hp[account] = account.habitipy().get_stats()['hp']
        for account in Account.objects.all():
            fuck_my_life(account)
