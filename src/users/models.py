# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MANAGER_LEVEL = (
	(0, 'PROJECT'),
	(1, 'SENIOR'),
	(2, 'EXECUTIVE'),
)

class AppUser(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	date_of_birth = models.DateField()
	joined_on = models.DateField()
	active = models.BooleanField(default=True)
	email = models.EmailField(max_length=256)
	employed_since = models.DateField()
	
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
	reports_to = models.ForeignKey('self',null=True,blank=True)
	designation = models.IntegerField(choices=MANAGER_LEVEL)

