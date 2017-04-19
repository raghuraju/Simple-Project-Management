# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from core.utils import get_upload_to_path


class Gender(models.Model):
	name = models.CharField(max_length=10, blank=False, null=False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural='Gender'


class ManagerDesignation(models.Model):
	name = models.CharField(max_length=10, blank=False, null=False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name='Designation'
		verbose_name_plural='Designations'


class AppUser(models.Model):
	date_of_birth = models.DateField()
	employed_since = models.DateField()
	picture = models.ImageField(null=True)
	gender = models.ForeignKey(Gender)
	user = models.OneToOneField(User,null=True)

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
	reports_to = models.ForeignKey('users.Executive', null=True, blank=True)
	designation = models.ForeignKey(ManagerDesignation)

	class Meta:
		verbose_name='Manager'
		verbose_name_plural='Managers'

class Executive(AppUser):
	designation = models.ForeignKey(ManagerDesignation)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



