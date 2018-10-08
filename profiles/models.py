import os, random
from datetime import date
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from rest_framework.reverse import reverse as api_reverse


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext

# def upload_image_path(instance, filename):
#     # print(instance)
#     print(filename)
#     new_filename = random.randint(1,391020931)
#     _name, ext = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     print(new_filename)
#     print(final_filename)
#     return "{new_filename}/{final_filename}".format(
#             new_filename=new_filename, 
#             final_filename=final_filename
#             )

class PlayerManager(models.Manager):
    def all(self):
        return self.get_queryset().filter(is_active=True)

class Player(models.Model):
    POSITION = (
        ('goalkeeper', 'GoalKeeper'), 
        ('defender', 'Defender'),
        ('midfielder' ,'MidFielder'), 
        ('forward' ,'Forawrd'))

    first_name      = models.CharField(max_length = 120, db_column='first_name', blank=True, null=True)
    last_name       = models.CharField(max_length = 120, db_column='last_name', blank=True, null=True)
    position        = models.CharField(max_length=10, choices=POSITION, default='MF', blank=True, null=True)
    birth_date      = models.DateField(default=date.today,blank=True, null=True)
    age             = models.IntegerField(blank=True, null=True)
    weight          = models.FloatField(blank=True, null=True)
    height          = models.FloatField(blank=True, null=True)
    image           = models.ImageField(upload_to='player/avatars/', null=True, blank=True)
    is_active       = models.BooleanField()

    objects = PlayerManager()

    class Meta:
        db_table = 'profiles_player'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['first_name']

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('players:detail', args=[self.pk])
    
    def get_api_url(self, request=None):
        return api_reverse("api-profiles:rud", kwargs={'pk': self.pk}, request=request)

def player_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.age:
        born = instance.birth_date
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        instance.age = age

pre_save.connect(player_pre_save_receiver, sender=Player) 


class PlayerAlias(models.Model):
    full_name       = models.ForeignKey('Player', on_delete=models.CASCADE)
    related_names   = models.CharField(max_length=255,blank=True, null=True, unique=True)

    class Meta:
        db_table = 'profiles_related_names'
        verbose_name = 'Related name'
        verbose_name_plural = 'Related names'
        ordering = ['related_names']

    def __str__(self):
        return self.related_names

    
