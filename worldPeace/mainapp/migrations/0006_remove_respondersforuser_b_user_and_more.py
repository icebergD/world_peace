# Generated by Django 4.1.3 on 2022-11-18 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_respondersforbusines_respondersforuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondersforuser',
            name='b_user',
        ),
        migrations.AddField(
            model_name='respondersforuser',
            name='vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.vacancy'),
            preserve_default=False,
        ),
    ]
