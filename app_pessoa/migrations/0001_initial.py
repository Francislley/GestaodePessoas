# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('dat_nasc', models.DateField()),
            ],
        ),
    ]
