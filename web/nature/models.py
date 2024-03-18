from django.db import models

# Create your models here.

class earthquake(models.Model):
    year = models.IntegerField("년도")
    damaged_buildings = models.FloatField("건물")
    damaged_ships = models.FloatField("선박")
    damaged_farms = models.FloatField("농경지")
    damaged_public = models.FloatField("공공시설")
    damaged_private = models.FloatField("사유시설")
    amount_of_damaged = models.FloatField("피해액합계")

class forest_fire_sido(models.Model):
    sido = models.CharField("시도", max_length = 10)
    cause = models.CharField("원인", max_length = 30, null = True)
    damaged_area = models.FloatField("피해면적")
    start_date = models.DateField("발생일시")
    end_date = models.DateField("종료일시")
    year = models.IntegerField("년도")

class forest_fire_money(models.Model):
    year = models.IntegerField("년도")
    number_of_cases = models.IntegerField("건수", null = True)
    damaged_area = models.IntegerField("피해면적", null = True)
    damaged_ratio_per_case = models.FloatField("건당피해", null = True) 
    damaged_trees = models.IntegerField("피해재적", null = True)
    amount_of_damaged = models.BigIntegerField("피해액")

class typhoon(models.Model):
    typhoon_name = models.CharField("태풍고유번호", max_length = 15)

class typhoon_location(models.Model):
    typhoon_name = models.CharField("태풍고유번호", max_length = 15)
    name = models.CharField("태풍이름", max_length = 15)
    latitude = models.FloatField("위도")
    longitude = models.FloatField("경도")
    rank = models.CharField("태풍등급", max_length = 5, null = True)
    date = models.DateTimeField("분석시각")
    year = models.IntegerField("년도")

class typhoon_money(models.Model):
    year = models.IntegerField("년도")
    damaged_buildings = models.FloatField("건물", null = True)
    damaged_ships = models.FloatField("선박", null = True)
    damaged_farms = models.FloatField("농경지", null = True)
    damaged_public = models.FloatField("공공시설", null = True)
    damaged_private = models.FloatField("사유시설", null = True)
    amount_of_damaged = models.FloatField("피해액합계")

class landslide_damaged(models.Model):
    sido = models.CharField("시도", max_length = 10)
    year_2011 = models.FloatField("2011")
    year_2012 = models.FloatField("2012")
    year_2013 = models.FloatField("2013")
    year_2014 = models.FloatField("2014")
    year_2015 = models.FloatField("2015")
    year_2016 = models.FloatField("2016")
    year_2017 = models.FloatField("2017")
    year_2018 = models.FloatField("2018")
    year_2019 = models.FloatField("2019")

class landslide_money(models.Model):
    year = models.IntegerField("년도")
    amount_of_damaged = models.BigIntegerField("피해액")

class landslide_sido_damaged(models.Model):
    YEAR_CHOICES = [
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
    ]
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, primary_key=True, default = 0)
    seoul = models.FloatField("서울", default=0.0)
    busan = models.FloatField("부산", default=0.0)
    daegu = models.FloatField("대구", default=0.0)
    incheon = models.FloatField("인천", default=0.0)
    gwangju = models.FloatField("광주", default=0.0)
    daejeon = models.FloatField("대전", default=0.0)
    ulsan = models.FloatField("울산", default=0.0)
    sejong = models.FloatField("세종", default=0.0)
    gyeonggi = models.FloatField("경기", default=0.0)
    chungbuk = models.FloatField("충북", default=0.0)
    chungnam = models.FloatField("충남", default=0.0)
    jeonnam = models.FloatField("전남", default=0.0)
    gyeongbuk = models.FloatField("경북", default=0.0)
    gyeongnam = models.FloatField("경남", default=0.0)
    jeju = models.FloatField("제주", default=0.0)
    gangwon = models.FloatField("강원", default=0.0)
    jeonbuk = models.FloatField("전북", default=0.0)