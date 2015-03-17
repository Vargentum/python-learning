# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name="ім'я")),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Записи', 'verbose_name': 'Запис', 'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='posts.Category', null=True, verbose_name='category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='вміст'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='час створення'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='опис'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='заголовок'),
            preserve_default=True,
        ),
    ]
