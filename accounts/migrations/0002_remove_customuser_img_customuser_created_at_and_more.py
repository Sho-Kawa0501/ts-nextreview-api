# Generated by Django 4.1.6 on 2023-02-19 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='img',
        ),
        migrations.AddField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='profile/default.png', null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='未設定', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
    ]
