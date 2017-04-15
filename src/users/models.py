# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.utils import get_upload_to_path

MANAGER_LEVEL = (
	(0, 'PROJECT'),
	(1, 'SENIOR'),
)

class AppUser(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	date_of_birth = models.DateField()
	joined_on = models.DateField()
	active = models.BooleanField(default=True)
	email = models.EmailField(max_length=256)
	employed_since = models.DateField()
	picture = models.ImageField(null=True)
	
	@property
	def experience(self):
		import datetime
		return datetime.datetime.now().year - self.employed_since.year	
	
	def __unicode__(self):
		return '{0} {1}'.format(self.first_name, self.last_name)
	
	class Meta:
		abstract = True

class Team(models.Model):
	name = models.CharField(max_length=30)
	incharge = models.ForeignKey('users.ProjectManager')

class Developer(AppUser):
	team = models.ForeignKey(Team)

class Designer(AppUser):
	team = models.ForeignKey(Team)

class Tester(AppUser):
	team = models.ForeignKey(Team)
	automation = models.BooleanField(default=False)

class ProjectManager(AppUser):
	reports_to = models.ForeignKey('users.Executive')
	designation = models.IntegerField(choices=MANAGER_LEVEL)

class Executive(AppUser):
	designation = models.IntegerField(choices=MANAGER_LEVEL)
