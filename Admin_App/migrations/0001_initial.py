# Generated by Django 4.2.3 on 2023-10-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.BooleanField(default=True)),
            ],
        ),
    ]