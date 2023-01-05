# Generated by Django 4.1.4 on 2022-12-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='n/a', max_length=6400)),
                ('job_title', models.CharField(default='n/a', max_length=6400)),
                ('contact_name', models.CharField(default='n/a', max_length=6400)),
                ('contact_number', models.CharField(default='n/a', max_length=6400)),
                ('email', models.CharField(default='n/a', max_length=6400)),
                ('company_website', models.CharField(default='n/a', max_length=6400)),
                ('address', models.CharField(default='n/a', max_length=6400)),
                ('linkedin', models.CharField(default='n/a', max_length=6400)),
                ('jobs', models.CharField(default='n/a', max_length=6400)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]