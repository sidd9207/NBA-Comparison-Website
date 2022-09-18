# Generated by Django 4.1.1 on 2022-09-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerNameOne', models.CharField(max_length=225)),
                ('playerNameTwo', models.CharField(max_length=225)),
                ('yearOptionOne', models.CharField(choices=[('2003-04', '2003-04'), ('2004-05', '2004-05'), ('2005-06', '2005-06'), ('2006-07', '2006-07'), ('2007-08', '2007-08'), ('2008-09', '2008-09'), ('2009-10', '2009-10'), ('2010-11', '2010-11'), ('2011-12', '2011-12'), ('2012-13', '2012-13'), ('2013-14', '2013-14'), ('2014-15', '2014-15'), ('2015-16', '2015-16'), ('2016-17', '2016-17'), ('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20'), ('2020-21', '2020-21'), ('2021-22', '2021-22')], default='0304', max_length=9)),
                ('yearOptionTwo', models.CharField(choices=[('2003-04', '2003-04'), ('2004-05', '2004-05'), ('2005-06', '2005-06'), ('2006-07', '2006-07'), ('2007-08', '2007-08'), ('2008-09', '2008-09'), ('2009-10', '2009-10'), ('2010-11', '2010-11'), ('2011-12', '2011-12'), ('2012-13', '2012-13'), ('2013-14', '2013-14'), ('2014-15', '2014-15'), ('2015-16', '2015-16'), ('2016-17', '2016-17'), ('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20'), ('2020-21', '2020-21'), ('2021-22', '2021-22')], default='0304', max_length=9)),
            ],
        ),
    ]
