# Generated by Django 3.2.13 on 2022-05-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_strategy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='acct_alias',
        ),
        migrations.AddField(
            model_name='strategy',
            name='ext_trade_id',
            field=models.IntegerField(default=-1, unique=True),
        ),
    ]