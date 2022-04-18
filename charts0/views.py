from django.shortcuts import render

from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi2.models import DPC0, TC0, MC0, DPCArea0, DPCDef0, DPCRemark0, MCArea0, MCDef0, MCRemark0, TCArea0, TCDef0, TCRemark0
from django.db.models import Avg, Sum
from django.utils import timezone
from django.contrib import messages
# Create your views here.

@login_required
def chartshome0(request):
    currdate = date.today()
    context = {
        'time': currdate,
    }
    return render(request, 'charts0/chartshome.html', context)


@login_required
def dpcchart0(request):
    if request.POST.get('datepicker') and request.POST.get('datepicker1'):
        RakeName = []
        BrakeBlock = []
        currdate = date.today()
        currmonth = currdate.month
        currmonth = currdate.month
        curryear = currdate.year
        yesterday = date.today() - timedelta(days=1)
        qs6 = DPC0.objects.all().order_by('-Date')
        qs2 = DPCArea0.objects.all()
        qs4 = DPCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker'), POHDate__gt=request.POST.get('datepicker1'))
        qs5 = DPCDef0.objects.all()
        defi = []
        for x in qs2:
            q = DPCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker'), POHDate__gt=request.POST.get('datepicker1')).filter(DPCDefArea=x.id).count()
            defi.append({str(x.DPCArea):q})
        print(defi)
        list2 = []
        for x in defi:
	        for key , value in list(x.items()):
		        if (value != 0):
			        list2.append(x)
        print(list2)
        message = messages.success(request, "Showing Chart !")
    else:
        message = messages.warning(request, "Please set dates first !")
        list1 = []
        defi = []
        currdate = date.today()
    
    
    context = {
        'time': currdate,
        'RolStock' : 'DPC',
        'from' : request.POST.get('datepicker1'),
        'to' : request.POST.get('datepicker'),
        'data' : list2,
        
    }
    return render(request, 'charts0/chartshome.html', context)

@login_required
def tcchart0(request):
    if request.POST.get('datepicker4') and request.POST.get('datepicker3'):
        currdate = date.today()
        currmonth = currdate.month
        currmonth = currdate.month
        curryear = currdate.year
        yesterday = date.today() - timedelta(days=1)
        qs6 = TC0.objects.all().order_by('-Date')
        qs2 = TCArea0.objects.all()
        qs4 = TCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
        qs5 = TCDef0.objects.all()
        defi = []
        for x in qs2:
            q = TCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3')).filter(TCDefArea=x.id).count()
            defi.append({str(x.TCCArea):q})
        print(defi)
        list2 = []
        for x in defi:
	        for key , value in list(x.items()):
		        if (value != 0):
			        list2.append(x)
        print(list2)
        message = messages.success(request, "Showing Chart !")
    else:
        message = messages.warning(request, "Please set dates first !")
        list1 = []
        defi = []
        currdate = date.today()
    
    context = {
        'time': currdate,
        'RolStock' : 'TC',
        'from' : request.POST.get('datepicker3'),
        'to' : request.POST.get('datepicker4'),
        'data' : list2,
        
    }
    return render(request, 'charts0/chartshome.html', context)


@login_required
def mcchart20(request):
    if request.POST.get('datepicker6') and request.POST.get('datepicker5'):
        currdate = date.today()
        currmonth = currdate.month
        currmonth = currdate.month
        curryear = currdate.year
        yesterday = date.today() - timedelta(days=1)
        qs6 = MC0.objects.all().order_by('-Date')
        qs2 = MCArea0.objects.all()
        qs4 = MCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5'))
        qs5 = MCDef0.objects.all()
        defi = []
        for x in qs2:
            q = MCRemark0.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5')).filter(MCDefArea=x.id).count()
            defi.append({str(x.MCArea):q})
        print(defi)
        print("************************************")
        list2 = []
        for x in defi:
	        for key , value in list(x.items()):
		        if (value != 0):
			        list2.append(x)
        print(list2)
        message = messages.success(request, "Showing Chart !")
    else:
        message = messages.warning(request, "Please set dates first !")
        list1 = []
        defi = []
        currdate = date.today()
    
    context = {
        'time': currdate,
        'data' : list2,
        'RolStock' : 'MC',
        'from' : request.POST.get('datepicker5'),
        'to' : request.POST.get('datepicker6'),
        
    }
    return render(request, 'charts0/chartshome.html', context)