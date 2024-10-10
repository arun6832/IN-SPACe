# Generated by Django 5.1 on 2024-10-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense_splitter_app', '0011_alter_member_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='split',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='member',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
