# Generated by Django 3.1.7 on 2021-05-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flashcard_title', models.CharField(max_length=50)),
                ('flashcard_word', models.CharField(max_length=50)),
                ('flashcard_definition', models.CharField(max_length=50)),
            ],
        ),
    ]
