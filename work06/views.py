# Create your views here.
from django.shortcuts import render
from .forms import ReiwaForm, BMIForm, WarikanForm, SavingsForm, CalculatorForm


def reiwa(request):
    result = None

    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["year"]
            seireki = 2018 + reiwa_year  # 令和元年 = 2019年
            result = f"令和{reiwa_year}年 = 西暦{seireki}年"
    else:
        form = ReiwaForm()

    return render(
        request,
        "work06/index.html",
        {"form": form, "result": result}
    )


def bmi(request):
    result = None
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height_cm = form.cleaned_data['height']
            height_m = height_cm / 100
            bmi = weight / (height_m * height_m)
            result = round(bmi, 2)
    else:
        form = BMIForm()
    return render(request, 'work06/bmi.html', {'form': form, 'result': result})


def warikan(request):
    result = None
    if request.method == "POST":
        form = WarikanForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data['total_amount']
            people = form.cleaned_data['people']
            result = round(total / people, 2)
    else:
        form = WarikanForm()
    return render(
        request,
        'work06/warikan.html',
        {'form': form, 'result': result}
    )


def savings(request):
    table = []
    if request.method == "POST":
        form = SavingsForm(request.POST)
        if form.is_valid():
            monthly = form.cleaned_data['monthly_amount']
            years = form.cleaned_data['years']
            
            total = 0
            for year in range(1, years + 1):
                total += monthly * 12
                table.append({'year': year, 'total': total})
    else:
        form = SavingsForm()
    return render(
        request,
        'work06/savings.html',
        {'form': form, 'table': table}
    )


def calculator(request):
    result = None
    error = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            op = form.cleaned_data['operation']
            try:
                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        error = "0で割ることはできません"
                    else:
                        result = num1 / num2
            except Exception as e:
                error = str(e)
    else:
        form = CalculatorForm()
    return render(
        request,
        'work06/calculator.html',
        {
            'form': form,
            'result': result,
            'error': error
        }
    )