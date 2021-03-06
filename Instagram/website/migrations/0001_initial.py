# Generated by Django 3.1.1 on 2020-12-28 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('biography', models.CharField(blank=True, max_length=200, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='pp/')),
                ('slug', models.SlugField(default='', null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('timePosted', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='djangodbmodelsfieldsautofield', editable=False, null=True, unique=True)),
                ('userPosted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timePosted'],
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('likeID', models.AutoField(primary_key=True, serialize=False)),
                ('onPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('followNumber', models.AutoField(primary_key=True, serialize=False)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentNumber', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=250)),
                ('timeCommented', models.DateTimeField(auto_now_add=True)),
                ('commentBy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commentedOn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
            ],
            options={
                'ordering': ['-timeCommented'],
            },
        ),
    ]
