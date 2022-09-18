from django.db import models
import pandas as pd
from nba_api.stats import endpoints
from nba_api.stats.static import players
import numpy as np
import requests



# Create your models here.


YEAR_CHOICES=(
    ('2003-04','2003-04'),
    ('2004-05','2004-05'),
    ('2005-06','2005-06'),
    ('2006-07','2006-07'),
    ('2007-08','2007-08'),
    ('2008-09','2008-09'),
    ('2009-10','2009-10'),
    ('2010-11','2010-11'),
    ('2011-12','2011-12'),
    ('2012-13','2012-13'),
    ('2013-14','2013-14'),
    ('2014-15','2014-15'),
    ('2015-16','2015-16'),
    ('2016-17','2016-17'),
    ('2017-18','2017-18'),
    ('2018-19','2018-19'),
    ('2019-20','2019-20'),
    ('2020-21','2020-21'),
    ('2021-22','2021-22'),
)
class Query (models.Model):
    playerNameOne = models.CharField(max_length=225)
    playerNameTwo = models.CharField(max_length=225)
    yearOptionOne = models.CharField(max_length=9,choices=YEAR_CHOICES,default='2003-2004')
    yearOptionTwo = models.CharField(max_length=9,choices=YEAR_CHOICES,default='2003-2004')





