# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Structure(models.Model):
    c = (
        (None, "Невідомо чи працює"),
        (True, "Працює"),
        (False, "Не працює"),
        )
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    work_status = models.NullBooleanField(choices = c)
    comment = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.name
    
    
    @property    
    def readable_work_status(self):
        c = dict(self.c)
        return c[self.work_status]
        
"""
    @property    
    def readable_work_status(self):
        if self.work_status == True:
            return u"Працює"
        elif self.work_status == False:
            return u"Не працює"
        else: 
            return u"Невідомо чи працює"
"""