# Generated by Django 4.2.7 on 2024-04-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='coach_images', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Coach',
                'verbose_name_plural': 'Coaches',
                'db_table': 'coaches2',
            },
        ),
    ]
