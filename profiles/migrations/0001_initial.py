# Generated by Django 2.0.6 on 2018-07-10 19:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, db_column='first_name', max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, db_column='last_name', max_length=120, null=True)),
                ('position', models.CharField(blank=True, choices=[('goalkeeper', 'GoalKeeper'), ('defender', 'Defender'), ('midfielder', 'MidFielder'), ('forward', 'Forawrd')], default='MF', max_length=10, null=True)),
                ('birth_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='player/avatars/')),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
                'db_table': 'profiles_player',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='PlayerAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_names', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Player')),
            ],
            options={
                'verbose_name': 'Related name',
                'verbose_name_plural': 'Related names',
                'db_table': 'profiles_related_names',
                'ordering': ['related_names'],
            },
        ),
    ]
