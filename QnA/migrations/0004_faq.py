# Generated by Django 5.0.4 on 2024-06-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0003_rename_product_id_question_item_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
            ],
        ),
    ]