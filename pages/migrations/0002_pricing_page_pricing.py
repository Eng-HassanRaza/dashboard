# Generated by Django 2.2.10 on 2021-02-09 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_team'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing_page',
            name='pricing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Pricing'),
        ),
    ]
