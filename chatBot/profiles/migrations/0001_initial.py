# Generated by Django 4.1 on 2022-08-19 21:50

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('relation', models.CharField(choices=[('family', 'Family'), ('friends', 'Friends'), ('work', 'Work'), ('partner', 'Partner'), ('unknown', 'Unknown')], max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=profiles.models.custom_upload_to)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
