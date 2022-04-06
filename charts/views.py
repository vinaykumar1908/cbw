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
    qs6 = DPC.objects.all().order_by('-Date').filter(Date__lt=timezone.now(), Date__gt=f'{curryear}-{currmonth}-01')
    qs2 = DPCArea.objects.all()
    qs4 = DPCRemark.objects.all().order_by('-Date').filter(Date__lt=timezone.now(), Date__gt=f'{curryear}-{currmonth}-01')
    
    list1 = []
    for x in qs6:
        w = qs4.filter(DPCName=x.id)
        list1.append(w)
        

    print(list1)
    context = {
        'RakeName': qs2,
        'time': currdate,    
    }
    return render(request, 'charts/chartshome.html', context)