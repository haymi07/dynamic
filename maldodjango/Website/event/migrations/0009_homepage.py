# Generated by Django 5.0.2 on 2024-02-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_remove_expriance_url_expriance_html_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
