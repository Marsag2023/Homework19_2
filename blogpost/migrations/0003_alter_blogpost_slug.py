# Generated by Django 5.0.4 on 2024-05-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_alter_blogpost_publication_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='slug'),
        ),
    ]
