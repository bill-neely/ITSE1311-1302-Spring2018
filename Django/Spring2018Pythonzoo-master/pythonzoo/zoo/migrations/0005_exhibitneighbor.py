# Generated by Django 2.0.4 on 2018-05-01 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitNeighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(blank=True, choices=[('n', 'North'), ('s', 'South'), ('w', 'West'), ('e', 'East'), ('nw', 'Northwest'), ('ne', 'Northeast'), ('sw', 'Southwest'), ('se', 'Southeast')], help_text='Enter Direction', max_length=2, null=True)),
                ('fromExhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fromExhibit', to='zoo.Exhibit')),
                ('toExhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toExhibit', to='zoo.Exhibit')),
            ],
        ),
    ]