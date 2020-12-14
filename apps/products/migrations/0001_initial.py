# Generated by Django 3.1.3 on 2020-12-14 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30)),
                ('sub_category_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('image', models.FileField(blank=True, null=True, upload_to='Products_Images/')),
                ('description', models.TextField(blank=True, max_length=400)),
                ('old_price', models.FloatField(default=0.0, verbose_name='Old Price')),
                ('new_price', models.FloatField(default=0.0, verbose_name='New Price')),
                ('discount', models.FloatField(default=0.0)),
                ('brand', models.CharField(blank=True, max_length=264)),
                ('code', models.CharField(blank=True, max_length=30)),
                ('availability', models.BooleanField(default=None, verbose_name='Quantity')),
                ('color', models.CharField(blank=True, max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='category', to='apps.products.category' )),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Products_Images/')),
                ('product', models.ForeignKey( default=None, on_delete=django.db.models.deletion.CASCADE, to='apps.products.product' )),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='apps.products.tag' ),
        ),
    ]