# Generated by Django 2.2.5 on 2020-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tops', '0003_auto_20201026_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertops',
            name='nickname',
            field=models.CharField(default='top', max_length=50),
        ),
    ]
