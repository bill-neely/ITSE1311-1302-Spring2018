# Generated by Django 2.0.4 on 2018-04-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_exhibit'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoo',
            name='logoFileName',
            field=models.CharField(help_text='Enter logo file name', max_length=200, null=True),
        ),
    ]
