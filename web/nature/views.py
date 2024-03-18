from django.shortcuts import render
from django.http import JsonResponse
from nature.models import typhoon, typhoon_location, typhoon_money, earthquake, landslide_damaged, landslide_money, forest_fire_sido, forest_fire_money
from django.db.models import Sum, Count 

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
    return render(request, 'landslide.html')


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

    context = {
        "sido" : sido,
        "sum" : sum,
        "count" : count,
        "year" : year,
        "money" : money,
    }
    return render(request, 'fires.html', context)



