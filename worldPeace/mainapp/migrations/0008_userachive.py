# Generated by Django 4.1.3 on 2022-11-19 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0007_busines_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.achive')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
