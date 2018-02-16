# Generated by Django 2.0.1 on 2018-02-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20180214_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('description', models.CharField(default='', max_length=250)),
                ('context', models.CharField(default='', max_length=100)),
                ('key_takeaways', models.CharField(default='', max_length=50)),
                ('sample_uses_and_visualization', models.CharField(default='', max_length=100)),
                ('technical_details', models.CharField(default='', max_length=100)),
                ('applicable_models', models.CharField(default='', max_length=100)),
                ('relevant_publications', models.CharField(default='', max_length=50)),
                ('contact_details', models.EmailField(default='example@gmail.com', max_length=50)),
                ('owner', models.CharField(default='', max_length=50)),
                ('published', models.BooleanField(default=True)),
                ('outcomes', models.ManyToManyField(to='data.Outcome')),
                ('parameters', models.ManyToManyField(to='data.Parameter')),
                ('scales', models.ManyToManyField(to='data.Scale')),
            ],
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='publish',
        ),
        migrations.AddField(
            model_name='dataset',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]