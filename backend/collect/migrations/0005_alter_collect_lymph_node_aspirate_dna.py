# Generated by Django 4.2.10 on 2024-07-08 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0004_collect_coat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='lymph_node_aspirate_dna',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]