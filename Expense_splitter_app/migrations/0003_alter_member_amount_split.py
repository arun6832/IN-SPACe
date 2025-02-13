# Generated by Django 5.1 on 2024-10-10 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense_splitter_app', '0002_alter_member_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='splits', to='Expense_splitter_app.group')),
            ],
        ),
    ]
