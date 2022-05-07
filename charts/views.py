from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from defi.models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, MCArea, MCDef, MCRemark, TCArea, TCDef, TCRemark, DPCSection, TCSection, MCSection
from django.db.models import Avg, Sum
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.http import JsonResponse

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
        
        list2 = []
        labels = []
        listx = []
        listm = []
        finallist = []
        currdate = date.today()
        if request.POST.get('DPC',None) == 'DPC':
            qs6 = DPC.objects.all().order_by('-Date')
            qs2 = DPCArea.objects.all()
            qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = DPCDef.objects.all()
            defi = []
            for x in qs2:
                q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(DPCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'DPC-{x.DPCArea}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'part'})
                    # print('defi')
                    # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print('list2')
            # print(list2)
            RolStock.append('DPC')
        if request.POST.get('DemuTC',None) == 'DemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='False')
            qs2 = TCArea.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            defi = []
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(TCName__Memu=False).filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'DemuTC-{x.TCCArea}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'part'})
            # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print(list2)
            RolStock.append('DemuTC')
        if request.POST.get('MemuTC',None) == 'MemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='True')
            g = qs6.first()
            # print("*(*(*((*(*((*(*")
            # print(g.Memu)
            # print('*(*(((*((*(**(')
            qs2 = TCArea.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            defi = []
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(TCName__Memu=True).filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'MemuTC-{x.TCCArea}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'part'})
            # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print(list2)
            RolStock.append('MemuTC')
        if request.POST.get('MC',None) == 'MC':
            # print('MC')
            qs6 = MC.objects.all().order_by('-Date')
            qs2 = MCArea.objects.all()
            qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = MCDef.objects.all()
            defi = []
            for x in qs2:
                q = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(MCDefArea=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'MC-{x.MCArea}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'part'})
            #print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    # print('**********HELLO********')
                    # print(key)
                    # print(value)
                    # print('**********HELLO********')
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend((x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"))
                        listx.append(listc)
                        list2.append(x)
                        print(listx)
                    else:
                        pass
            # print(list2)
            RolStock.append('MC')
    currdate = date.today()
    # print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    # print(list2)
    # print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    message = messages.success(request, f"Showing Failed Parts Chart for {RolStock}, from {request.POST.get('datepicker3')}, to {request.POST.get('datepicker4')}, with threshold {threshold}")
    context = {
        'time': currdate,
        'RolStock' : RolStock,
        'from' : request.POST.get('datepicker3'),
        'to' : request.POST.get('datepicker4'),
        'labels': labels,
        'data' : list2,
        'threshold' : threshold,
        'listx': listx,
        'listm' : listm,
        'message' : message,
        
    }
    # print('ttttttttttttttt')
    # print(context['labels'])
    # print('rrrrrrrrrrrrrrr')
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
        
        list2 = []
        labels = []
        listx = []
        listm = []
        finallist = []
        currdate = date.today()
        if request.POST.get('DPC',None) == 'DPC':
            qs6 = DPC.objects.all().order_by('-Date')
            qs2 = DPCSection.objects.all()
            qs4 = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = DPCDef.objects.all()
            defi = []
            for x in qs2:
                q = DPCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'DPC-{x.Section}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'section'})
                    # print('defi')
                    # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print('list2')
            # print(list2)
            RolStock.append('DPC')
        if request.POST.get('DemuTC',None) == 'DemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='False')
            qs2 = TCSection.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            defi = []
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(TCName__Memu=False).filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'DemuTC-{x.Section}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'section'})
            # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print(list2)
            RolStock.append('DemuTC')
        if request.POST.get('MemuTC',None) == 'MemuTC':
            qs6 = TC.objects.all().order_by('-Date').filter(Memu='True')
            g = qs6.first()
            # print("*(*(*((*(*((*(*")
            # print(g.Memu)
            # print('*(*(((*((*(**(')
            qs2 = TCSection.objects.all()
            qs4 = TCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = TCDef.objects.all()
            defi = []
            for x in qs2:
                q = TCRemark.objects.all().order_by('-POHDate').filter(TCName__Memu=True).filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'MemuTC-{x.Section}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'section'})
            # print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend([x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"])
                        listx.append(listc)
                        list2.append(x)
                    else:
                        pass
            # print(list2)
            RolStock.append('MemuTC')
        if request.POST.get('MC',None) == 'MC':
            # print('MC')
            qs6 = MC.objects.all().order_by('-Date')
            qs2 = MCSection.objects.all()
            qs4 = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
            qs5 = MCDef.objects.all()
            defi = []
            for x in qs2:
                q = MCRemark.objects.all().order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=x.id).count()
                if q >= int(threshold):
                    defi.append({"Name":f'MC-{x.Section}','Val':q, 'D1':date1, 'D2':date2, 'd3':x.id, 'side':'section'})
            #print(defi)
            list2 = []
            for x in defi:
                for key , value in x.items():
                    # print('**********HELLO********')
                    # print(key)
                    # print(value)
                    # print('**********HELLO********')
                    if key == 'Val' and value > 0:
                        labels.append(f"{x.get('Name')}")
                        listc = []
                        listm.append(x.get('Val'))
                        listc.extend((x.get('Val'),f"{x.get('Name')}",f"{x.get('D1')}",f"{x.get('D2')}",f"{x.get('d3')}",f"{x.get('side')}"))
                        listx.append(listc)
                        list2.append(x)
                        print(listx)
                    else:
                        pass
            # print(list2)
            RolStock.append('MC')
    currdate = date.today()
    # print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    # print(list2)
    # print('!!!!!!!!!!!!!!!!!^^^^^^^^^^^^^^')
    message = messages.success(request, f"Showing Failed Section Chart for {RolStock}, from {request.POST.get('datepicker3')}, to {request.POST.get('datepicker4')}, with threshold {threshold}")
    context = {
        'time': currdate,
        'RolStock2' : RolStock,
        'from' : request.POST.get('datepicker'),
        'to' : request.POST.get('datepicker1'),
        'labels': labels,
        'data' : list2,
        'threshold' : threshold,
        'listx': listx,
        'listm' : listm,
        'message' : message,
        
    }
    # print('ttttttttttttttt')
    # print(context['labels'])
    # print('rrrrrrrrrrrrrrr')
    return render(request, 'charts/chartshome.html', context)

@csrf_exempt
@login_required
def partsdata(request):
    global xy
    print(request.method)
    if request.method == 'POST':
        name=request.POST.get('headline')
        email=request.POST.get('tag')
        D1=request.POST.get('D1')
        D2=request.POST.get('D2')
        side=request.POST.get('side')
        print(f'{name} {email} {D1} {D2}')
        xy = {'name':name, 'email':email, 'D1':D1, 'D2':D2, 'side':side}
        
        # iteration(request, 1,2)
        return JsonResponse(xy, safe=False)
    else:
        print(request.method)
        print(xy)
        y = xy
        name = y.get('name')
        print(name)
        name = name.split('-')
        print(name)
        name1 = name[0]
        print(name1)
        surname = name[1]
        date1 = y.get('D1')
        date2 = y.get('D2')
        print('000000000000000')
        print(date1)
        print(date2)
        print('000000000000000')
        print(type(surname))
        print(y.get('side'))
        list1 = []
        list2 = []
        if xy.get('side') == 'part':
            if name1 == 'DPC':
                t = DPCArea.objects.all().filter(DPCArea__iexact=surname)
                w = DPCRemark.objects.all().order_by("-POHDate").filter(POHDate__lt=date2, POHDate__gt=date1).filter(DPCDefArea=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for DPC art {surname} complete for {date1} to {date2}.")
            elif name1 == 'DemuTC':
                t = TCArea.objects.all().filter(TCCArea__iexact=surname)
                w = TCRemark.objects.all().order_by("-POHDate").filter(TCName__Memu=False).filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for Demu TC part {surname} complete for {date1} to {date2}.")
            elif name1 == 'MemuTC':
                t = TCArea.objects.all().filter(TCCArea__iexact=surname)
                w = TCRemark.objects.all().order_by("-POHDate").filter(TCName__Memu=True).filter(POHDate__lt=date2, POHDate__gt=date1).filter(TCDefArea=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for Memu TC part{surname} complete for {date1} to {date2}.")
            elif name1 == 'MC':
                t = MCArea.objects.all().filter(MCArea__iexact=surname)
                w = MCRemark.objects.all().order_by("-POHDate").filter(POHDate__lt=date2, POHDate__gt=date1).filter(MCDefArea=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for MC part {surname} complete for {date1} to {date2}.")
        elif xy.get('side') == 'section':
            if name1 == 'DPC':
                t = DPCSection.objects.all().filter(Section__iexact=surname)
                print(surname)
                print(t)
                w = DPCRemark.objects.all().order_by("-POHDate").filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for DPC section {surname} complete for {date1} to {date2}.")
            elif name1 == 'DemuTC':
                print(str(surname))
                t = TCSection.objects.all().filter(Section__iexact=surname)
                print(t)
                w = TCRemark.objects.all().order_by("-POHDate").filter(TCName__Memu=False).filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for Demu TC section {surname} complete for {date1} to {date2}.")
            elif name1 == 'MemuTC':
                t = TCSection.objects.all().filter(Section__iexact=surname)
                w = TCRemark.objects.all().order_by("-POHDate").filter(TCName__Memu=True).filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for Memu TC section {surname} complete for {date1} to {date2}.")
            elif name1 == 'MC':
                t = MCSection.objects.all().filter(Section__icontains=str(surname))
                print(surname)
                print(t)
                w = MCRemark.objects.all().order_by("-POHDate").filter(POHDate__lt=date2, POHDate__gt=date1).filter(Section=t[0].id)
                for x in w:
                    list1.append(x)
                message = messages.success(request, f"Search for MC section {surname} complete for {date1} to {date2}")
        context = {
        'test': y.get('name'),
        'data': list1,
        'side': y.get('side'),
        # 'message': message,
        }
        print(list1)
        return render(request, 'deficiencies/deflisthome.html', context)
