# Generated by Django 4.0.4 on 2022-05-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0003_alter_checkout_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_choice',
            field=models.CharField(choices=[('1', 'Dropoff'), ('2', 'Pickup')], max_length=100, verbose_name='checkout choice'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='checkout time'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_room',
            field=models.CharField(max_length=20, verbose_name='class room'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='day_of_week',
            field=models.CharField(max_length=20, verbose_name='day of week'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='end_time',
            field=models.TimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='start_time',
            field=models.TimeField(verbose_name='start time'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(max_length=100, verbose_name='teacher name'),
        ),
    ]