# Generated by Django 3.2.20 on 2024-01-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]
