# Generated by Django 4.1.4 on 2022-12-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_leads_address_alter_leads_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='address',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='company_name',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='company_website',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='contact_name',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='contact_number',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='email',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='job_title',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='jobs',
            field=models.TextField(default='n/a'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='linkedin',
            field=models.TextField(default='n/a'),
        ),
    ]
