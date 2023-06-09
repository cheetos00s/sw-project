# Generated by Django 4.2.1 on 2023-06-02 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_country_ciudad_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics/%y/%m/%d/')),
                ('title', models.CharField(max_length=150)),
                ('action_name', models.CharField(max_length=50)),
                ('link', models.TextField(blank=True, null=True)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]
