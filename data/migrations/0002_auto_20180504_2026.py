# Generated by Django 2.0.1 on 2018-05-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='applicable_models_or_datasets',
            field=models.TextField(default='', max_length=750),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='context',
            field=models.TextField(default='', max_length=750),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='key_takeaways',
            field=models.TextField(default='', max_length=750),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='relevant_publications',
            field=models.TextField(default='', max_length=750),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='slug',
            field=models.SlugField(default='', max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='technical_details',
            field=models.TextField(default='', max_length=750),
        ),
    ]
