# Generated by Django 3.0.5 on 2020-04-21 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('role', models.IntegerField(choices=[(1, 'admin'), (2, 'user')], default=2, help_text='User type')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specialist.Category')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specialist.SubCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
