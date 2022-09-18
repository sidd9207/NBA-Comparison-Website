# Generated by Django 4.1.1 on 2022-09-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbaWebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='yearOptionOne',
            field=models.CharField(choices=[('2003-04', '2003-04'), ('2004-05', '2004-05'), ('2005-06', '2005-06'), ('2006-07', '2006-07'), ('2007-08', '2007-08'), ('2008-09', '2008-09'), ('2009-10', '2009-10'), ('2010-11', '2010-11'), ('2011-12', '2011-12'), ('2012-13', '2012-13'), ('2013-14', '2013-14'), ('2014-15', '2014-15'), ('2015-16', '2015-16'), ('2016-17', '2016-17'), ('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20'), ('2020-21', '2020-21'), ('2021-22', '2021-22')], default='2003-2004', max_length=9),
        ),
        migrations.AlterField(
            model_name='query',
            name='yearOptionTwo',
            field=models.CharField(choices=[('2003-04', '2003-04'), ('2004-05', '2004-05'), ('2005-06', '2005-06'), ('2006-07', '2006-07'), ('2007-08', '2007-08'), ('2008-09', '2008-09'), ('2009-10', '2009-10'), ('2010-11', '2010-11'), ('2011-12', '2011-12'), ('2012-13', '2012-13'), ('2013-14', '2013-14'), ('2014-15', '2014-15'), ('2015-16', '2015-16'), ('2016-17', '2016-17'), ('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20'), ('2020-21', '2020-21'), ('2021-22', '2021-22')], default='2003-2004', max_length=9),
        ),
    ]