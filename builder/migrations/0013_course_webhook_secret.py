# Generated by Django 2.2.25 on 2022-01-04 13:42

import builder.models
from django.db import migrations, models


def populate_secrets(apps, schema_editor):
    for course in builder.models.Course.objects.all():
        course.reset_webhook_secret()
        course.save()


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0012_auto_20220103_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='webhook_secret',
            field=models.CharField(default=None, max_length=64, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='webhook_secret',
            field=models.CharField(default=builder.models.generate_secret, max_length=64, unique=True, null=True),
        ),
    ]
