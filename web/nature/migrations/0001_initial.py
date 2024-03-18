# Generated by Django 5.0.3 on 2024-03-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="earthquake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(verbose_name="년도")),
                ("damaged_buildings", models.FloatField(verbose_name="건물")),
                ("damaged_ships", models.FloatField(verbose_name="선박")),
                ("damaged_farms", models.FloatField(verbose_name="농경지")),
                ("damaged_public", models.FloatField(verbose_name="공공시설")),
                ("damaged_private", models.FloatField(verbose_name="사유시설")),
                ("amount_of_damaged", models.FloatField(verbose_name="피해액합계")),
            ],
        ),
        migrations.CreateModel(
            name="forest_fire_money",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(verbose_name="년도")),
                ("number_of_cases", models.IntegerField(null=True, verbose_name="건수")),
                ("damaged_area", models.IntegerField(null=True, verbose_name="피해면적")),
                (
                    "damaged_ratio_per_case",
                    models.FloatField(null=True, verbose_name="건당피해"),
                ),
                ("damaged_trees", models.IntegerField(null=True, verbose_name="피해재적")),
                ("amount_of_damaged", models.BigIntegerField(verbose_name="피해액")),
            ],
        ),
        migrations.CreateModel(
            name="forest_fire_sido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sido", models.CharField(max_length=10, verbose_name="시도")),
                (
                    "cause",
                    models.CharField(max_length=30, null=True, verbose_name="원인"),
                ),
                ("damaged_area", models.FloatField(verbose_name="피해면적")),
                ("start_date", models.DateField(verbose_name="발생일시")),
                ("end_date", models.DateField(verbose_name="종료일시")),
                ("year", models.IntegerField(verbose_name="년도")),
            ],
        ),
        migrations.CreateModel(
            name="landslide_damaged",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sido", models.CharField(max_length=10, verbose_name="시도")),
                ("year_2011", models.FloatField(verbose_name="2011")),
                ("year_2012", models.FloatField(verbose_name="2012")),
                ("year_2013", models.FloatField(verbose_name="2013")),
                ("year_2014", models.FloatField(verbose_name="2014")),
                ("year_2015", models.FloatField(verbose_name="2015")),
                ("year_2016", models.FloatField(verbose_name="2016")),
                ("year_2017", models.FloatField(verbose_name="2017")),
                ("year_2018", models.FloatField(verbose_name="2018")),
                ("year_2019", models.FloatField(verbose_name="2019")),
            ],
        ),
        migrations.CreateModel(
            name="landslide_money",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(verbose_name="년도")),
                ("amount_of_damaged", models.BigIntegerField(verbose_name="피해액")),
            ],
        ),
        migrations.CreateModel(
            name="landslide_sido_damaged",
            fields=[
                (
                    "year",
                    models.CharField(
                        choices=[
                            ("2011", "2011"),
                            ("2012", "2012"),
                            ("2013", "2013"),
                            ("2014", "2014"),
                            ("2015", "2015"),
                            ("2016", "2016"),
                            ("2017", "2017"),
                            ("2018", "2018"),
                            ("2019", "2019"),
                        ],
                        default=0,
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("seoul", models.FloatField(default=0.0, verbose_name="서울")),
                ("busan", models.FloatField(default=0.0, verbose_name="부산")),
                ("daegu", models.FloatField(default=0.0, verbose_name="대구")),
                ("incheon", models.FloatField(default=0.0, verbose_name="인천")),
                ("gwangju", models.FloatField(default=0.0, verbose_name="광주")),
                ("daejeon", models.FloatField(default=0.0, verbose_name="대전")),
                ("ulsan", models.FloatField(default=0.0, verbose_name="울산")),
                ("sejong", models.FloatField(default=0.0, verbose_name="세종")),
                ("gyeonggi", models.FloatField(default=0.0, verbose_name="경기")),
                ("chungbuk", models.FloatField(default=0.0, verbose_name="충북")),
                ("chungnam", models.FloatField(default=0.0, verbose_name="충남")),
                ("jeonnam", models.FloatField(default=0.0, verbose_name="전남")),
                ("gyeongbuk", models.FloatField(default=0.0, verbose_name="경북")),
                ("gyeongnam", models.FloatField(default=0.0, verbose_name="경남")),
                ("jeju", models.FloatField(default=0.0, verbose_name="제주")),
                ("gangwon", models.FloatField(default=0.0, verbose_name="강원")),
                ("jeonbuk", models.FloatField(default=0.0, verbose_name="전북")),
            ],
        ),
        migrations.CreateModel(
            name="typhoon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "typhoon_name",
                    models.CharField(max_length=15, verbose_name="태풍고유번호"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="typhoon_location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "typhoon_name",
                    models.CharField(max_length=15, verbose_name="태풍고유번호"),
                ),
                ("name", models.CharField(max_length=15, verbose_name="태풍이름")),
                ("latitude", models.FloatField(verbose_name="위도")),
                ("longitude", models.FloatField(verbose_name="경도")),
                (
                    "rank",
                    models.CharField(max_length=5, null=True, verbose_name="태풍등급"),
                ),
                ("date", models.DateTimeField(verbose_name="분석시각")),
                ("year", models.IntegerField(verbose_name="년도")),
            ],
        ),
        migrations.CreateModel(
            name="typhoon_money",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField(verbose_name="년도")),
                ("damaged_buildings", models.FloatField(null=True, verbose_name="건물")),
                ("damaged_ships", models.FloatField(null=True, verbose_name="선박")),
                ("damaged_farms", models.FloatField(null=True, verbose_name="농경지")),
                ("damaged_public", models.FloatField(null=True, verbose_name="공공시설")),
                ("damaged_private", models.FloatField(null=True, verbose_name="사유시설")),
                ("amount_of_damaged", models.FloatField(verbose_name="피해액합계")),
            ],
        ),
    ]
