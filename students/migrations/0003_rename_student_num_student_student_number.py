# Generated by Django 4.2 on 2023-04-07 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_student_number_student_student_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_num',
            new_name='student_number',
        ),
    ]