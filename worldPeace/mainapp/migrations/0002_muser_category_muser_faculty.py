# Generated by Django 4.1.3 on 2022-11-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
        ),
        migrations.AddField(
            model_name='muser',
            name='faculty',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
