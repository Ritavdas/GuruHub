# Generated by Django 3.0.4 on 2021-04-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guruhub', '0005_auto_20210328_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
