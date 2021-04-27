# Generated by Django 3.1.5 on 2021-04-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guruhub', '0006_auto_20210428_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='about',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='pic',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='rate',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='star',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='taught',
            field=models.IntegerField(blank=True),
        ),
    ]
