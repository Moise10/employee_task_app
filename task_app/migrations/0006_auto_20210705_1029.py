# Generated by Django 3.2.5 on 2021-07-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0005_auto_20210705_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.userprofile'),
        ),
        migrations.AlterField(
            model_name='task',
            name='organisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='task_app.userprofile'),
            preserve_default=False,
        ),
    ]