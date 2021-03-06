# Generated by Django 3.2.7 on 2021-10-02 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HomePage', '0008_auto_20210827_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('ratings', models.CharField(max_length=1)),
                ('date', models.DateField(auto_now=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usern', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
