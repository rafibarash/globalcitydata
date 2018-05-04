# Generated by Django 2.0.1 on 2018-05-04 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('title', models.CharField(default='', max_length=50, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('description', models.CharField(default='', max_length=250)),
                ('context', models.CharField(default='', max_length=100)),
                ('key_takeaways', models.CharField(default='', max_length=50)),
                ('sample_uses_and_visualization', models.CharField(default='', max_length=100)),
                ('technical_details', models.CharField(default='', max_length=100)),
                ('applicable_models_or_datasets', models.CharField(default='', max_length=100)),
                ('relevant_publications', models.CharField(default='', max_length=50)),
                ('contact_details', models.EmailField(default='example@gmail.com', max_length=50)),
                ('owner', models.CharField(default='', max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Well Being', 'Well Being'), ('Health', 'Health'), ('Environment', 'Environment'), ('Equity', 'Equity'), ('Livability', 'Livability')], default='', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Social', 'Social'), ('Environment', 'Environment'), ('Infrastructure', 'Infrastructure'), ('Urban Design', 'Urban Design')], default='', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Intra Urban', 'Intra Urban'), ('Whole City', 'Whole City'), ('National Urban', 'National Urban')], default='', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Snapshot', 'Snapshot'), ('Time Series', 'Time Series'), ('Futures Modeling', 'Futures Modeling')], default='', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('Dataset', 'Dataset'), ('Model', 'Model')], default='', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorldRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('US', 'US'), ('China', 'China'), ('India', 'India')], default='', max_length=25, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='outcomes',
            field=models.ManyToManyField(to='data.Outcome'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='parameters',
            field=models.ManyToManyField(to='data.Parameter'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='spatial_scales',
            field=models.ManyToManyField(to='data.Scale'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='temporal_scales',
            field=models.ManyToManyField(to='data.Time'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Type'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='world_regions',
            field=models.ManyToManyField(to='data.WorldRegions'),
        ),
    ]
