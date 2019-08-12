# Generated by Django 2.2.3 on 2019-08-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamesh', '0009_logicmodulemodel_is_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='key',
            field=models.SlugField(help_text="The key in the response body, where the related object data will be saved into, p.e.: 'contact_siteprofile_relationship'.", max_length=64),
        ),
    ]
