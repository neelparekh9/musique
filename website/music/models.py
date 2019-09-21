# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
	artist= models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	genre=models.CharField(max_length=100)
	album_logo=models.CharField(max_length=2000)

	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.album_title +' - '+self.artist


class Song(models.Model):
	album=models.ForeignKey(Album, on_delete=models.CASCADE)#Foreignkey is used to link this to Albums.
	file_type=models.FileField()
	song_title=models.CharField(max_length=500)
	is_favourite=models.BooleanField(default=False)

	

	def __str__(self):
		return self.song_title
