# Generated by Django 4.2.10 on 2024-05-19 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breed', '0002_breed_specie'),
        ('coat', '0001_initial'),
        ('animal', '0004_animal_age_alter_animal_breed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='breed.breed'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='coat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coat.coat'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(blank=True, choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, null=True),
        ),
    ]