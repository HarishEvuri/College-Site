# Generated by Django 3.1.2 on 2020-11-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_attendance_attendanceclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(default='CSO-211', on_delete=django.db.models.deletion.CASCADE, to='Home.course'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
