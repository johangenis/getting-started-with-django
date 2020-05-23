# Generated by Django 3.0.5 on 2020-05-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200523_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('E', 'Error'), ('N', 'Not reviewed'), ('R', 'Reviewed'), ('A', 'Accepted')], max_length=1),
        ),
    ]