# Generated by Django 3.2.6 on 2022-05-03 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(choices=[('Кот', 'Кот'), ('Собака', 'Собака')], max_length=255, verbose_name='тип животного')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Адресс')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('type', models.CharField(max_length=255, verbose_name='тип')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.species')),
            ],
        ),
    ]