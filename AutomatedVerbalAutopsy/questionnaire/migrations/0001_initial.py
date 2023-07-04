# Generated by Django 4.1.7 on 2023-06-30 11:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marehemu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jina_kwanza', models.CharField(max_length=255)),
                ('jina_pili', models.CharField(max_length=255)),
                ('jina_mwisho', models.CharField(max_length=255)),
                ('jinsia', models.CharField(choices=[('mume', 'mwanaume'), ('mke', 'mwanamke')], max_length=255)),
                ('ndoa', models.CharField(choices=[('ndoa', 'ndoa'), ('hajafunga ndoa', 'hajafunga ndoa'), ('mjane', 'mjane'), ('mgane', 'mgane'), ('talaka', 'talaka'), ('kutengana', 'kutengana')], max_length=255)),
                ('kuzaliwa', models.DateField(default=django.utils.timezone.now)),
                ('kufa', models.DateField(default=django.utils.timezone.now)),
                ('mahali', models.CharField(choices=[('nyumbani', 'nyumbani'), ('hospitali', 'hospitali'), ('kituo cha afya', 'kituo cha afya'), ('sijui', 'sijui')], max_length=255)),
                ('maelezo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shuhuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('simu', models.CharField(default='', max_length=100)),
                ('uhusiano', models.CharField(choices=[('Baba', 'Baba'), ('Mama', 'Mama'), ('ndugu', 'ndugu'), ('Hakuna Uhusiano', 'Hakuna Uhusiano'), ('Nyingine', 'nyingine')], max_length=255)),
                ('uhusiano_kipindi_kifo', models.CharField(choices=[('Ndio', 'Ndio'), ('Hapana', 'Hapana')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sababu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sababu', models.CharField(max_length=255)),
                ('Marehemu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.marehemu', verbose_name='Sababu_Ya_Kifo')),
            ],
        ),
        migrations.AddField(
            model_name='marehemu',
            name='shuhuda',
            field=models.ManyToManyField(to='questionnaire.shuhuda', verbose_name='Shhuda_Wa_Kifo'),
        ),
    ]
