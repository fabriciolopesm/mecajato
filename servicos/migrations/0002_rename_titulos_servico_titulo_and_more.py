# Generated by Django 4.1.7 on 2023-03-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='titulos',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]
