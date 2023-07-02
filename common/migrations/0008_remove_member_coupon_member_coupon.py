# Generated by Django 4.2.2 on 2023-07-01 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_coupon_coupon_name'),
        ('common', '0007_alter_member_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='coupon',
        ),
        migrations.AddField(
            model_name='member',
            name='coupon',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon.coupon'),
        ),
    ]