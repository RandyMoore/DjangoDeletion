# Generated by Django 2.2.4 on 2019-08-01 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManyToManyParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToOneParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OneToOneParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='delete_example.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='delete_example.OrderReport'),
        ),
        migrations.CreateModel(
            name='OneToOneChildProtect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='child_protect', to='delete_example.OneToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='OneToOneChildNull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_null', to='delete_example.OneToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='OneToOneChildCascade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='child_cascade', to='delete_example.OneToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToOneChildProtect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children_protect', to='delete_example.ManyToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToOneChildNull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_null', to='delete_example.ManyToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToOneChildCascade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_cascade', to='delete_example.ManyToOneParent')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToManyChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents', models.ManyToManyField(related_name='children', to='delete_example.ManyToManyParent')),
            ],
        ),
    ]
