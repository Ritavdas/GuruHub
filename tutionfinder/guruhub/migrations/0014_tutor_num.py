# Generated by Django 3.0.4 on 2021-05-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guruhub', '0013_remove_tutor_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
