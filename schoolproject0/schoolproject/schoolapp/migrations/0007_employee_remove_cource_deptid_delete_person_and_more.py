# Generated by Django 4.1.3 on 2023-01-09 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0006_department_remove_person_cource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('deptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.department')),
            ],
        ),
        migrations.RemoveField(
            model_name='cource',
            name='deptid',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='cource',
        ),
    ]
