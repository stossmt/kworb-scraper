# Generated by Django 2.0.6 on 2018-09-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default='00000000')),
                ('position', models.IntegerField(blank=True, default='0', null=True)),
                ('position_change', models.IntegerField(blank=True, default='0', null=True)),
                ('artist', models.TextField(blank=True, default='null', max_length=200, null=True)),
                ('title', models.TextField(blank=True, default='null', max_length=200, null=True)),
                ('spins', models.IntegerField(blank=True, default='0', null=True)),
                ('spins_change', models.IntegerField(blank=True, default='0', null=True)),
                ('bullet', models.IntegerField(blank=True, default='0', null=True)),
                ('bullet_change', models.IntegerField(blank=True, default='0', null=True)),
                ('audience', models.DecimalField(blank=True, decimal_places=3, default='0', max_digits=10, null=True)),
                ('audience_change', models.DecimalField(blank=True, decimal_places=3, default='0', max_digits=10, null=True)),
                ('days', models.IntegerField(blank=True, default='0', null=True)),
                ('peak', models.IntegerField(blank=True, default='0', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('date_created', 'title')},
        ),
    ]
