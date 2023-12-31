# Generated by Django 4.2.5 on 2023-09-26 06:39

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_chat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True, verbose_name='Slug'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
