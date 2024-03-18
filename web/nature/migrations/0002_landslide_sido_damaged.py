# Generated by Django 5.0.3 on 2024-03-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nature", "0001_initial"),
    ]

    operations = [
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
    ]
