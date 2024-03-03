# Generated by Django 4.2.10 on 2024-03-03 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=55, unique=True)),
                ('body', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'sketch'), (2, 'published')], default=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
    ]