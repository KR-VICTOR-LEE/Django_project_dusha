# Generated by Django 4.2.2 on 2023-06-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_coupon_coupon_name'),
        ('common', '0005_remove_member_coupon_member_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='coupon',
            field=models.ManyToManyField(blank=True, null=True, to='coupon.coupon'),
        ),
    ]