# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

TASK_STATUS = (
	(0,'Pending'),
	(1,'Started'),
	(2,'Finished'),
	(3,'Testing'),
	(4,'Released'),
)

class Task(models.Model):
	name = models.TextField(blank=False, null=False)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	due_by = models.DateTimeField(blank=False,null=True)
	status = models.IntegerField(choices=TASK_STATUS,default='Pending')
	story_points = models.IntegerField(default=1)
	epic = models.ForeignKey('tasks.Epic')
	
	@property
	def ice_box(self):
		return self.status == 0
	
	def __unicode__(self):
		return "{0}, {1}, {2}".format(self.name, self.epic, self.epic.project)
		

class Epic(models.Model):
	name = models.CharField(max_length=30,blank=True,null=True)
	start_date = models.DateField()
	end_date = models.DateField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	project = models.ForeignKey('tasks.Project')
	
	def __unicode__(self):
		return "{0}, {1}".format(self.name, self.project)


class Project(models.Model):
	name = models.CharField(max_length=30)
	team = models.ForeignKey('users.Team',blank=True,null=True)
	
	def __unicode__(self):
		return self.name

