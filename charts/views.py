from django.shortcuts import render

from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, MCArea, MCDef, MCRemark, TCArea, TCDef, TCRemark
from django.db.models import Avg, Sum
from django.utils import timezone
from django.contrib import messages
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
    if request.POST.get('datepicker') and request.POST.get('datepicker1'):
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
            q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker'), POHDate__gt=request.POST.get('datepicker1')).filter(DPCDefArea=x.id).count()
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
    return render(request, 'charts/chartshome.html', context)

@login_required
def tcchart(request):
    if request.POST.get('datepicker4') and request.POST.get('datepicker3'):
        currdate = date.today()
        currmonth = currdate.month
        currmonth = currdate.month
        curryear = currdate.year
        yesterday = date.today() - timedelta(days=1)
        qs6 = TC.objects.all().order_by('-Date')
        qs2 = TCArea.objects.all()
        qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
        qs5 = TCDef.objects.all()
        defi = []
        for x in qs2:
            q = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3')).filter(TCDefArea=x.id).count()
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
    return render(request, 'charts/chartshome.html', context)


@login_required
def mcchart2(request):
    if request.POST.get('datepicker6') and request.POST.get('datepicker5'):
        currdate = date.today()
        currmonth = currdate.month
        currmonth = currdate.month
        curryear = currdate.year
        yesterday = date.today() - timedelta(days=1)
        qs6 = MC.objects.all().order_by('-Date')
        qs2 = MCArea.objects.all()
        qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5'))
        qs5 = MCDef.objects.all()
        defi = []
        for x in qs2:
            q = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=request.POST.get('datepicker6'), POHDate__gt=request.POST.get('datepicker5')).filter(MCDefArea=x.id).count()
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
    return render(request, 'charts/chartshome.html', context)