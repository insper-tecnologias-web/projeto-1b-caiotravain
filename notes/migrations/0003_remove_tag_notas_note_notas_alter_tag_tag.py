# Generated by Django 4.1 on 2022-09-20 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='Notas',
        ),
        migrations.AddField(
            model_name='note',
            name='Notas',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='notes.tag'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='Tag',
            field=models.CharField(max_length=100),
        ),
    ]