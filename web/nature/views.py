from django.shortcuts import render
from django.http import JsonResponse
from nature.models import typhoon, typhoon_location, typhoon_money, earthquake, landslide_damaged, landslide_money,landslide_sido_damaged, forest_fire_sido, forest_fire_money
from django.db.models import Sum, Count 
from datetime import datetime


# Create your views here.

def typhoon_page(request):
    typhoon_money_all = typhoon_money.objects.all()
    labels = []
    values = []

    for item in typhoon_money_all:
        labels.append(item.year)
        values.append(item.amount_of_damaged)
    context = {
        "labels" : labels,
        "values" : values,
    }

    return render(request, 'typhoon.html', context)


def earthquake_page(request):
    return render(request, 'earthquake.html')

def landslide_page(request):
    field_names = []
    totals = []

    # 2011~2019년동안의 시도별 총 산사태 피해면적을 위한 데이터
    for i in range(1, 18):  
        # 시도명
        field_name = landslide_sido_damaged._meta.get_fields()[i].name
        # 피해면적
        total = landslide_sido_damaged.objects.aggregate(total_amount=Sum(field_name))['total_amount']
        totals.append(total)
        field_names.append(field_name) 

    # 산사태 피해액 그래프를 위한 데이터
    # 년도
    years = []
    # 피해액
    amounts = []
    for item in landslide_money.objects.all():
        years.append(item.year)
        amounts.append(item.amount_of_damaged)

    context = {
        "field_names" : field_names,
        "totals" : totals,
        "years" : years,
        "amounts" : amounts
    }
    return render(request, 'landslide.html', context)



def fires_page(request):
    data = forest_fire_sido.objects.all().values('sido').annotate(count=Count('*')).annotate(sum=Sum("damaged_area"))
    
    sido = [item['sido'] for item in data]
    sum = [item['sum'] for item in data]
    count = [item['count'] for item in data]

    fires_money_all = forest_fire_money.objects.all()
    year = []
    money = []
    for item in fires_money_all:
        year.append(item.year)
        money.append(item.amount_of_damaged)
    # 2017년이상 2023년이하인 데이터만 필터링해서 시도별 산불 빈도수 추출하기
    year17to23 = forest_fire_sido.objects.filter(year__gte=2017,  year__lte=2023).values("sido").annotate(count_17to23=Count('*'))
    # 시도별로 따로담기
    sido17to23 = [item['sido'] for item in year17to23]
    # 빈도수 따로 담기
    count17to23 = [item['count_17to23'] for item in year17to23]


    context = {
        "sido" : sido,
        "sum" : sum,
        "count" : count,
        "year" : year,
        "money" : money,
        "sido17to23" : sido17to23,
        "count17to23" : count17to23,
    }
    return render(request, 'fires.html', context)



