from django.shortcuts import render

from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, MCArea, MCDef, MCRemark, TCArea, TCDef, TCRemark
from django.db.models import Avg, Sum
from django.utils import timezone
# Create your views here.

@login_required
def chartshome(request):
    currdate = date.today()
    context = {
        'time': currdate,
    }
    return render(request, 'charts/chartshome.html', context)


@login_required
def dpcchart(request):
    RakeName = []
    BrakeBlock = []
    currdate = date.today()
    currmonth = currdate.month
    currmonth = currdate.month
    curryear = currdate.year
    yesterday = date.today() - timedelta(days=1)
    qs6 = DPC.objects.all().order_by('-Date')
    qs2 = DPCArea.objects.all()
    qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker'), POHDate__gt=request.POST.get('datepicker1'))
    qs5 = DPCDef.objects.all()
    defi = []
    for x in qs2:
        defi.append(str(x.DPCArea))
    print(defi)
    list1 = []
    for x in qs2:
        q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker'), POHDate__gt=request.POST.get('datepicker1')).filter(DPCDefArea=x.id).count()
        print(q)
        list1.append(str(q))
        print('appended list')
        print(list1)
    
    
    context = {
        'DPC': defi,
        'time': currdate,
        'freq': list1 ,
        'RolStock' : 'DPC',
        'from' : request.POST.get('datepicker1'),
        'to' : request.POST.get('datepicker')
    }
    return render(request, 'charts/chartshome.html', context)

@login_required
def tcchart(request):
    RakeName = []
    BrakeBlock = []
    currdate = date.today()
    currmonth = currdate.month
    currmonth = currdate.month
    curryear = currdate.year
    yesterday = date.today() - timedelta(days=1)
    qs6 = TC.objects.all().order_by('-Date')
    qs2 = TCArea.objects.all()
    qs4 = TCRemark.objects.all().order_by('-Date').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
    qs5 = TCDef.objects.all()
    defi = []
    for x in qs2:
        defi.append(str(x.TCCArea))
    print(defi)
    list1 = []
    for x in qs2:
        q = TCRemark.objects.all().filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3')).filter(TCDefArea=x.id).count()
        print(q)
        list1.append(str(q))
        print('appended list')
        print(list1)
    
    context = {
        'DPC': defi,
        'time': currdate,
        'freq': list1,
        'RolStock' : 'TC',
        'from' : request.POST.get('datepicker3'),
        'to' : request.POST.get('datepicker4')
    }
    return render(request, 'charts/chartshome.html', context)


@login_required
def mcchart(request):
    RakeName = []
    BrakeBlock = []
    currdate = date.today()
    currmonth = currdate.month
    currmonth = currdate.month
    curryear = currdate.year
    yesterday = date.today() - timedelta(days=1)
    qs6 = MC.objects.all().order_by('-Date')
    qs2 = MCArea.objects.all()
    qs4 = MCRemark.objects.all().order_by('-Date').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5'))
    qs5 = MCDef.objects.all()
    defi = []
    for x in qs2:
        defi.append(str(x.MCArea))
    print(defi)
    list1 = []
    for x in qs2:
        q = MCRemark.objects.all().filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5')).filter(MCDefArea=x.id).count()
        print(q)
        list1.append(str(q))
        print('appended list')
        print(list1)
    
    context = {
        'DPC': defi,
        'time': currdate,
        'freq': list1,
        'RolStock' : 'MC',
        'from' : request.POST.get('datepicker5'),
        'to' : request.POST.get('datepicker6')
    }
    return render(request, 'charts/chartshome.html', context)