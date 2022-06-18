# Generated by Django 3.2.9 on 2022-06-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_drive_url', models.URLField()),
                ('youtube_url', models.URLField()),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshops.workshops')),
            ],
        ),
    ]