# Generated by Django 2.2 on 2021-02-16 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_management_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('briefdescription', models.CharField(max_length=255)),
                ('stepwise', models.CharField(max_length=255)),
                ('directions', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=255)),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
