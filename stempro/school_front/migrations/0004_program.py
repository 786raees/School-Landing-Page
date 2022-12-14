# Generated by Django 4.1.1 on 2022-09-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_front', '0003_alter_indexpage_main_heading_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_image', models.ImageField(default='static/images/uploads/early-elementary-hero-2880x1428.1575476978_2x.jpg', upload_to='uploads', verbose_name='Hero Image')),
                ('heading_1', models.CharField(default='Start Early. Learn Deeply.', max_length=150, verbose_name='Main Heading')),
                ('description_1', models.TextField(default='Spark an early interest in mathematics and lay the groundwork for higher level reasoning.', verbose_name='Main Description')),
                ('heading_2', models.CharField(default='We nurture the natural flexibility and curiosity of young minds to spark an interest in math and lay the foundations of higher level reasoning and logical thinking.', max_length=450, verbose_name='Sub Heading')),
                ('description_2', models.TextField(default='Young children are naturally curious, uninhibited, and can easily grasp very complex ideas. Our curriculum and methodology are built with this in mind. Our students learn to work with, and develop an appetite for, challenging mathematical concepts.', verbose_name='Sub Description')),
            ],
        ),
    ]
