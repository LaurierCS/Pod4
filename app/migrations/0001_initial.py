# Generated by Django 3.1.13 on 2022-05-17 01:46

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
            name='Skill',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('icon_HREF', models.URLField()),
                ('node_type', models.CharField(choices=[('C', 'Category'), ('N', 'Node'), ('U', 'User')], default='C', max_length=40)),
                ('parentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=100)),
                ('last_name', models.CharField(default='Doe', max_length=100)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, default='images/smiley.jpg', upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('E', 'Exploration'), ('P', 'Project'), ('L', 'Learning'), ('H', 'Hackathon'), ('Ev', 'Event')], default='E', max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('likes_amount', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('project_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
                ('skills', models.ManyToManyField(to='app.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='DesiredSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.FloatField(choices=[(0, 'Aiming to Learn'), (1, 'Some Understanding'), (2, 'Some Proficiency'), (3, 'Capable'), (4, 'Able to Use Professionally'), (5, 'Expert')], default=0)),
                ('description', models.TextField(max_length=1000)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.skill')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]
