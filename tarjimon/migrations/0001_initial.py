# Generated by Django 3.2.5 on 2021-07-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inglizcha', models.CharField(max_length=128, verbose_name='Inglizcha')),
                ('uzbekcha', models.CharField(max_length=128, verbose_name='O`zbekcha')),
            ],
        ),
    ]
