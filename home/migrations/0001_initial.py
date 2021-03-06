# Generated by Django 3.1.2 on 2020-12-30 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=9)),
                ('notes', models.TextField(blank=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.TextField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=9)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('position', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=10)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.locations')),
            ],
        ),
        migrations.CreateModel(
            name='projectTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_order', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('scope_work', models.TextField()),
                ('purchase_order', models.CharField(blank=True, max_length=15)),
                ('final_report', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.projects')),
            ],
        ),
        migrations.CreateModel(
            name='scheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_togo', models.DateField()),
                ('time_togo', models.TimeField()),
                ('notes', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.projecttasks')),
            ],
        ),
        migrations.CreateModel(
            name='taskstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='userTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedulerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.scheduler')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='taskCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.taskstatus')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.projecttasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='project_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='home.taskstatus'),
        ),
        migrations.AddField(
            model_name='projects',
            name='sales_rep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
