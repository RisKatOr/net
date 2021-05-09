# Generated by Django 3.1.7 on 2021-05-02 18:10

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='profile/photo/default.jpg', upload_to='profile/photo/', verbose_name='Fotoğraf')),
                ('bio', models.CharField(max_length=255, verbose_name='Biyografi')),
                ('web', models.URLField(verbose_name='Web')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('youtube', models.URLField(verbose_name='Youtube')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profil',
            },
        ),
    ]
