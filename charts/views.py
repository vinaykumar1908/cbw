from django.shortcuts import render

from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, MCArea, MCDef, MCRemark, TCArea, TCDef, TCRemark, DPCSection, TCSection, MCSection
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
def partschart(request):
    if request.method == 'POST':
        date1 = request.POST.get('datepicker3')
        date2 = request.POST.get('datepicker4')
        threshold = request.POST.get('threshold')
        if threshold == '':
            threshold = 0
        print(f"{date1}****{date2}*****{threshold}******{request.POST.get('DPC',None)}{request.POST.get('TC',None)}{request.POST.get('MC',None)}{request.POST.get('DemuTC',None)}{request.POST.get('MemuTC',None)}")
        RolStock = []
        list1 = []
        defi = []
        list2 = []
        currdate = date.today()
        if request.POST.get('DPC',None) == 'DPC':
            qs6 = DPC.objects.all().order_by('-Date')
            qs2 = DPCArea.objects.all()
            qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = DPCDef.objects.all()
            for x in qs2:
                q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(DPCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({f'DPC-{x.DPCArea}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('DPC')
        if request.POST.get('DemuTC',None) == 'DemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='False')
            qs2 = TCArea.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({f'DemuTC-{x.TCCArea}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('DemuTC')
        if request.POST.get('MemuTC',None) == 'MemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='True')
            g = qs6.first()
            print("*(*(*((*(*((*(*")
            print(g.Memu)
            print('*(*(((*((*(**(')
            qs2 = TCArea.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({f'MemuTC-{x.TCCArea}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('MemuTC')
        if request.POST.get('MC',None) == 'MC':
            print('MC')
            qs6 = MC.objects.all().order_by('-Date')
            qs2 = MCArea.objects.all()
            qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = MCDef.objects.all()
            for x in qs2:
                q = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(MCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({f'MC-{x.MCArea}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('MC')
    currdate = date.today()
    print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    print(list2)
    print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    message = messages.success(request, f"Showing Failed Parts Chart for {RolStock}, from {request.POST.get('datepicker3')}, to {request.POST.get('datepicker4')}, with threshold {threshold}")
    context = {
        'time': currdate,
        'RolStock' : RolStock,
        'from' : request.POST.get('datepicker3'),
        'to' : request.POST.get('datepicker4'),
        'data' : list2,
        'threshold' : threshold,
        
    }
    return render(request, 'charts/chartshome.html', context)


@login_required
def sectionchart(request):
    if request.method == 'POST':
        date1 = request.POST.get('datepicker')
        date2 = request.POST.get('datepicker1')
        threshold = request.POST.get('threshold')
        if threshold == '':
            threshold = 0
        print(f"{date1}****{date2}*****{threshold}******{request.POST.get('DPC',None)}{request.POST.get('TC',None)}{request.POST.get('MC',None)}{request.POST.get('DemuTC',None)}{request.POST.get('MemuTC',None)}")
        RolStock = []
        list1 = []
        defi = []
        list2 = []
        currdate = date.today()
        if request.POST.get('DPC',None) == 'DPC':
            qs6 = DPC.objects.all().order_by('-Date')
            qs2 = DPCSection.objects.all()
            qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = DPCDef.objects.all()
            for x in qs2:
                q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({f'DPC-{x.Section}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('DPC')
        if request.POST.get('DemuTC',None) == 'DemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='False')
            qs2 = TCSection.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({f'DemuTC-{x.Section}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('DemuTC')
        if request.POST.get('MemuTC',None) == 'MemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='True')
            g = qs6.first()
            print("*(*(*((*(*((*(*")
            print(g.Memu)
            print('*(*(((*((*(**(')
            qs2 = TCSection.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({f'MemuTC-{x.Section}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('MemuTC')
        if request.POST.get('MC',None) == 'MC':
            print('MC')
            qs6 = MC.objects.all().order_by('-Date')
            qs2 = MCSection.objects.all()
            qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = MCDef.objects.all()
            for x in qs2:
                q = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({f'MC-{x.Section}':q})
            print(defi)
            list2 = []
            for x in defi:
                for key , value in list(x.items()):
                    if (value != 0):
                        list2.append(x)
            print(list2)
            RolStock.append('MC')
    
    currdate = date.today()
    print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    print(list2)
    print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    message = messages.success(request, f"Showing Section Failure Chart for {RolStock}, from {request.POST.get('datepicker')}, to {request.POST.get('datepicker1')}, with threshold {threshold}")
    context = {
        'time': currdate,
        'RolStock2' : RolStock,
        'from' : request.POST.get('datepicker3'),
        'to' : request.POST.get('datepicker4'),
        'data' : list2,
        'threshold' : threshold,
        'message' : message,
        
    }
    return render(request, 'charts/chartshome.html', context)