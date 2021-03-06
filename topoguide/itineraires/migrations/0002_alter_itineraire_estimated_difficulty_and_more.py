# Generated by Django 4.0.4 on 2022-04-21 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraire',
            name='estimated_difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')]),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1/5'), (2, '2/5'), (3, '3/5'), (4, '4/5'), (5, '5/5')], verbose_name='Difficulté ressentie'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='group_xp',
            field=models.CharField(choices=[('NOOB', 'Tous débutants'), ('MIX', 'Mixte'), ('EXPERIENCED', 'Tous Expérimentés')], max_length=20, verbose_name='Expérience des participants à la sortie'),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='weather',
            field=models.CharField(choices=[('GD', 'Bonne'), ('AVG', 'Moyenne'), ('BAD', 'Mauvaise')], max_length=8, verbose_name='Météo'),
        ),
    ]
