# Generated by Django 4.1.3 on 2022-11-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.tag', verbose_name='Теги'),
        ),
    ]
