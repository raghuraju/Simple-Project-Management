# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (Team, Developer, Designer, Tester, ProjectManager, Gender, ManagerDesignation)

admin.site.register(Team)
admin.site.register(Developer)
admin.site.register(Designer)
admin.site.register(Tester)
admin.site.register(ProjectManager)
admin.site.register(Gender)
admin.site.register(ManagerDesignation)

