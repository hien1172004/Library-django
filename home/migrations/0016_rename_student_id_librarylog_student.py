# Generated by Django 5.1.2 on 2024-11-08 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_student_librarylog_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarylog',
            old_name='student_id',
            new_name='student',
        ),
    ]
