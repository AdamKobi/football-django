from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.conf import settings

import datetime


class Injury(models.Model):
    # id = models.AutoField(primary_key=True)
    athlete             = models.ForeignKey('profiles.Player', on_delete=models.CASCADE)
    date_of_injury      = models.DateField(default=datetime.date.today, verbose_name='Date of injury')
    date_of_return      = models.DateField(default=datetime.date.today, verbose_name='Date of return')
    participation       = models.ForeignKey(on_delete=models.CASCADE, to='injuries.Participate')
    injured_body_part   = models.ForeignKey(on_delete=models.CASCADE, to='injuries.InjuredBodyPart')
    left_right          = models.ForeignKey(on_delete=models.CASCADE, verbose_name='Left/Right', to='injuries.LeftRight')
    type_of_injury      = models.ForeignKey(on_delete=models.CASCADE, to='injuries.TypeOfInjury')
    where_it_happened   = models.ForeignKey(on_delete=models.CASCADE, to='injuries.WhereItHappened')
    cause_of_injury     = models.ForeignKey(on_delete=models.CASCADE, to='injuries.CauseOfInjury')
    contact_collision   = models.ForeignKey(on_delete=models.CASCADE, verbose_name='Contact/Collison', to='injuries.ContactCollison')
    mechanism           = models.ForeignKey(on_delete=models.CASCADE, to='injuries.Mechanism')
    place_of_injury     = models.ForeignKey(on_delete=models.CASCADE, to='injuries.PlaceOfInjury')
    created_by          = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
    update              = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'injuries_injury'
        verbose_name = 'Injury'
        verbose_name_plural = 'Injuries'
        ordering = ['-date_of_injury']
        

    def __str__(self):
        return "%s %s" % (self.athlete, self.date_of_injury)

    def get_absolute_url(self):
        return reverse('injuries:detail', args=[self.pk])
    
    @property
    def owner(self):
        return self.created_by
    
    def get_api_url(self, request=None):
        return api_reverse("injuries:injury-rud", kwargs={'pk': self.pk}, request=request)

class Participate(models.Model):
    participate         = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_participate'
        verbose_name = 'Participation'
        verbose_name_plural = 'Participation'

    def __str__(self):
        return self.participate

class InjuredBodyPart(models.Model):
    injured_body_part = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_injuredbodypart'
        verbose_name = 'Injured body part'
        verbose_name_plural = 'Injured body parts'

    def __str__(self):
        return self.injured_body_part

class LeftRight(models.Model):
    left_right = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_leftright'
        verbose_name = 'Left/Right'
        verbose_name_plural = 'Right/Left'

    def __str__(self):
        return self.left_right
    
class TypeOfInjury(models.Model):    
    type_of_injury      = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_typeofinjury'
        verbose_name = 'Type of injuriy'
        verbose_name_plural = 'Type of injuries'

    def __str__(self):
        return self.type_of_injury
    
class WhereItHappened(models.Model):    
    where_it_happened   = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_whereithappened'
        verbose_name = 'Where it happened'
        verbose_name_plural = 'Where it happened'

    def __str__(self):
        return self.where_it_happened
    
class CauseOfInjury(models.Model):    
    cause_of_injury     = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_causeofinjury'
        verbose_name = 'Cause of injury'
        verbose_name_plural = 'Cause of injuries'

    def __str__(self):
        return self.cause_of_injury
    
class ContactCollison(models.Model):    
    contact_collision   = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_contactcollison'
        verbose_name = 'Contact/Collision'
        verbose_name_plural = 'Contacts/Collisions'

    def __str__(self):
        return self.contact_collision
    
class Mechanism(models.Model):    
    mechanism           = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_mechanism'
        verbose_name = 'Mechnism'
        verbose_name_plural = 'Mechnisms'

    def __str__(self):
        return self.mechanism

class PlaceOfInjury(models.Model):    
    place_of_injury         = models.CharField(max_length=255)

    class Meta:
        db_table = 'injuries_placeofinjury'
        verbose_name = 'Place of injury'
        verbose_name_plural = 'places of injury'

    def __str__(self):
        return self.place_of_injury
