# Generated by Django 4.2.10 on 2024-03-24 16:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('breed', '0002_breed_specie'),
        ('coat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('id_db_original', models.CharField(max_length=5)),
                ('name_chip', models.CharField(max_length=15)),
                ('sex', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1)),
                ('breed', models.ForeignKey(default='402b24bb-0c72-4e20-8c5a-343adbc73ce9', on_delete=django.db.models.deletion.CASCADE, to='breed.breed')),
                ('coat', models.ForeignKey(default='7fb2be2e-fb77-40c7-973b-fe6040e9daef', on_delete=django.db.models.deletion.CASCADE, to='coat.coat')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
                'ordering': ('-name',),
            },
        ),
    ]
