from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, TCArea, TCDef, TCRemark, MCArea, MCDef, MCRemark, DPCSection, TCSection, MCSection
from django.contrib import messages
from django.http import JsonResponse
from io import BytesIO
import pandas as pd
from openpyxl import Workbook
import dateutil.parser
from datetime import timedelta, date
from django.http import HttpResponse
# Create your views here.



class DefiHome(LoginRequiredMixin, TemplateView):
    template_name = 'deficiencies/defhome.html'



@login_required
def DefiHome2(request):
    dpc = DPC.objects.all().order_by('-POHDate')
    tc = TC.objects.all().order_by('-POHDate')
    mc = MC.objects.all().order_by('-POHDate')
        
        
    context = {
            'dpc': dpc,
            'tc' : tc,
            'mc' : mc,
    }
    print('successful')
    return render(request, 'deficiencies/defhome.html', context)

@login_required
def Exporthome(request):
    context = {
            
    }
    print('successful')
    return render(request, 'deficiencies/export.html', context)

@login_required
def ExportExcel(request):
    if request.method == 'POST':
        threshold = request.POST.get('threshold')
        date1 = request.POST.get('datepicker3')
        date2 = request.POST.get('datepicker4')
        if threshold == '':
            threshold = 0
        print(f"{date1}****{date2}*****{threshold}******{request.POST.get('DPC',None)}{request.POST.get('TC',None)}{request.POST.get('MC',None)}{request.POST.get('DemuTC',None)}{request.POST.get('MemuTC',None)}")
        RolStock = []
        list1 = []
        defi = []
        list2 = []
        currdate = date.today()
        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter', options={'remove_timezone': True})
            if request.POST.get('DPC',None) == 'DPC':
                data1 = pd.DataFrame(list(DPCRemark.objects.order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).values('Date','POHDate','DPCName__DPCName','DPCDefArea__DPCArea','DPCDef__DPCDef', 'Section__Section')))
                print(data1)
                data1['Date'] = data1['Date'].dt.tz_localize(None)
                #data1['POHDate'] = data1['POHDate'].dt.tz_localize(None)
                # data1['TKDOutTime'] = data1['TKDOutTime'].dt.tz_localize(None)
                # data1['YardInTime'] = data1['YardInTime'].dt.tz_localize(None)
                # data1['YardOutTime'] = data1['YardOutTime'].dt.tz_localize(None)
                # data1['MechanicalDetention'] = data1['MechanicalDetention'].dt.total_seconds()/60
                # data1['SidingDetention'] = data1['SidingDetention'].dt.total_seconds()/60
                # data1['TrafficDetention'] = data1['TrafficDetention'].dt.total_seconds()/60
                print(data1.dtypes)
                data1.to_excel(writer, sheet_name=f'DPC {date1}-{date2}')
            if request.POST.get('DemuTC',None) == 'DemuTC':
                a = TC.objects.all().order_by('-Date').filter(Memu='False')
                q = TCRemark.objects.all()
                w = q.order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
                list1 = []
                for x in a:
                    p = q.filter(TCName=x.id)
                    for r in p:
                        list1.append({"Date":r.Date,"Type":'Demu TC',"TCName":r.TCName,"POHDate":r.POHDate,"Section":r.Section,"TCDefArea":r.TCDefArea,"TCDef":r.TCDef})
                data2 = pd.DataFrame(list1 , columns = ['Date','POHDate','TCName','Type','TCDefArea','TCDef', 'Section'])
                data2['Date'] = data2['Date'].dt.tz_localize(None)
                data2.to_excel(writer, sheet_name=f'DemuTC {date1}-{date2}')
            if request.POST.get('MemuTC',None) == 'MemuTC':
                a = TC.objects.all().order_by('-Date').filter(Memu='True')
                q = TCRemark.objects.all()
                w = q.order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1)
                list1 = []
                for x in a:
                    p = q.filter(TCName=x.id)
                    for r in p:
                        list1.append({"Date":r.Date,"Type":'Memu TC',"TCName":r.TCName,"POHDate":r.POHDate,"Section":r.Section,"TCDefArea":r.TCDefArea,"TCDef":r.TCDef})
                data3 = pd.DataFrame(list1 , columns = ['Date','POHDate','TCName','Type','TCDefArea','TCDef', 'Section'])
                data3['Date'] = data3['Date'].dt.tz_localize(None)
                data3.to_excel(writer, sheet_name=f'MemuTC {date1}-{date2}')
            if request.POST.get('MC',None) == 'MC':
                data4 = pd.DataFrame(list(MCRemark.objects.order_by('-POHDate').filter(POHDate__lt=date2, POHDate__gt=date1).values('Date','POHDate','MCName__MCName','MCDefArea__MCArea','MCDef__MCDef', 'Section__Section')))
                print(data4)
                data4['Date'] = data4['Date'].dt.tz_localize(None)
                #data2['POHDate'] = data2['POHDate'].dt.tz_localize(None)
                print(data4.dtypes)
                data4.to_excel(writer, sheet_name=f'MC {date1}-{date2}')
            writer.save()
            filename = f'IC0 Deficiencies from {date1} to {date2}'
            content_type = 'application/vnd.ms-excel'
            response = HttpResponse(b.getvalue(), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="' + filename + '.xlsx"'
            return response


@login_required
def AddDPC(request):
    if request.method == 'POST' and request.POST.get('DPCNum').startswith("DPC")==True and request.POST.get('datepicker1'):
        print(request.POST.get('datepicker1'))
        newDPC = DPC(DPCName=request.POST.get('DPCNum'),POHDate=request.POST.get('datepicker1'),author=request.user)
        newDPC.save()
        message = messages.success(request, "DPC Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        tc = TC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "DPC Not Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        tc = TC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    

@login_required
def AddTC(request):
    print(request.POST.get('TCNum'))
    print(request.POST.get('datepicker'))
    print(request.POST.get('Memu'))
    g = True
    if request.POST.get('Memu') == 'on':
        g = True
    else:
        g = False
    print(g)
    if request.method == 'POST' and request.POST.get('TCNum').startswith("TC")==True and request.POST.get('datepicker'):
        print(request.POST.get('datepicker'))
        newTC = TC(TCName=request.POST.get('TCNum'),POHDate=request.POST.get('datepicker'),author=request.user, Memu=g)
        newTC.save()
        message = messages.success(request, "TC Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        tc = TC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        print(newTC.Memu)
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "TC Not Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        tc = TC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    
@login_required
def AddMC(request):
    if request.method == 'POST' and request.POST.get('MCNum').startswith("MC")==True and request.POST.get('datepicker2'):
        newMC = MC(MCName=request.POST.get('MCNum'),POHDate=request.POST.get('datepicker2'),author=request.user)
        newMC.save()
        message = messages.success(request, "MC Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        tc = TC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                'message' : message,
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "TC Not Added ")
        dpc = DPC.objects.all().order_by('-POHDate')
        mc = MC.objects.all().order_by('-POHDate')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    

@login_required
def showDPCdet(request, Serial):
    q = DPC.objects.get(id=Serial)
    print("--------------------**------------------")
    print(q)
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)

@login_required
def showTCdet(request, Serial):
    print("--------------------**------------------")
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-POHDate')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)

@login_required
def showMCdet(request, Serial):
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-POHDate')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)


@login_required
def addDPCpart(request, Serial):
    q = DPC.objects.get(id=Serial)
    if DPCArea.objects.filter(DPCArea=request.POST.get('addDPCpart')).exists():
        message = messages.warning(request, "DPC Part already exists ")
        p = DPCRemark.objects.filter(DPCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/dpcdefdet.html', context)
        pass
    if request.method == 'POST':
        newPart = DPCArea(DPCArea=request.POST.get('addDPCpart'))
        newPart.save()
        print(newPart)
        message = messages.success(request, "DPC Part '{}' Added ".format(newPart))
    else:
        message = messages.warning(request, "DPC Part Not Added ")
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)

@login_required
def addDPCdef(request, Serial):
    q = DPC.objects.get(id=Serial)
    if DPCDef.objects.filter(DPCDef=request.POST.get('addDPCdef')).exists():
        message = messages.warning(request, "DPC Deficiency already exists ")
        p = DPCRemark.objects.filter(DPCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/dpcdefdet.html', context)
        pass
    if request.method == 'POST':
        newDef = DPCDef(DPCDef=request.POST.get('addDPCdef'))
        newDef.save()
        print(newDef)
        message = messages.success(request, "DPC Deficiency '{}'  Added ".format(newDef))
    else:
        message = messages.warning(request, "DPC Deficiency Not Added ")
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)


@login_required
def addDPCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def') and request.POST.get('Section'):
        q = DPC.objects.filter(id=Serial).first()
        
        r = DPCArea.objects.filter(DPCArea=request.POST.get('Part')).first()
        t = DPCDef.objects.filter(DPCDef=request.POST.get('Def')).first()
        y = DPCSection.objects.filter(Section=request.POST.get('Section')).first()
        if request.method == 'POST':
            newDef = DPCRemark(DPCName=q, DPCDefArea=r, DPCDef=t, POHDate=q.POHDate, Section=y)
            newDef.save()
            print(newDef)
            print(newDef.DPCName)
            print(newDef.DPCDefArea)
            print(newDef.DPCDef)
            print(newDef.DPCDef)
            message = messages.success(request, "DPC Deficiency Record  Added: {} --> {} --> {}".format(newDef.DPCName, newDef.DPCDefArea, newDef.DPCDef))
        else:
            message = messages.warning(request, "DPC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill all Entries ")

    
    p = DPC.objects.get(id=Serial)
    q = DPCRemark.objects.filter(DPCName=p.id).order_by('-POHDate')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)

@login_required
def addTCpart(request, Serial):
    q = TC.objects.get(id=Serial)
    if TCArea.objects.filter(TCCArea=request.POST.get('addTCpart')).exists():
        message = messages.warning(request, "TC Part already exists ")
        p = TCRemark.objects.filter(TCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/tcdefdet.html', context)
        pass
    if request.method == 'POST':
        newPart = TCArea(TCCArea=request.POST.get('addTCpart'))
        newPart.save()
        print(newPart)
        message = messages.success(request, "TC Part '{}' Added ".format(newPart))
    else:
        message = messages.warning(request, "TC Part Not Added ")
    p = TCRemark.objects.filter(TCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)

@login_required
def addTCdef(request, Serial):
    q = TC.objects.get(id=Serial)
    if TCDef.objects.filter(TCDef=request.POST.get('addTCdef')).exists():
        message = messages.warning(request, "TC Deficiency already exists ")
        p = TCRemark.objects.filter(TCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/tcdefdet.html', context)
        pass
    if request.method == 'POST':
        newDef = TCDef(TCDef=request.POST.get('addTCdef'))
        newDef.save()
        print(newDef)
        message = messages.success(request, "TC Deficiency '{}'  Added ".format(newDef))
    else:
        message = messages.warning(request, "TC Deficiency Not Added ")
    p = TCRemark.objects.filter(TCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)


@login_required
def addTCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def') and request.POST.get('Section'):
        q = TC.objects.filter(id=Serial).first()
        r = TCArea.objects.filter(TCCArea=request.POST.get('Part')).first()
        t = TCDef.objects.filter(TCDef=request.POST.get('Def')).first()
        y = TCSection.objects.filter(Section=request.POST.get('Section')).first()
        if request.method == 'POST':
            newDef = TCRemark(TCName=q, TCDefArea=r, TCDef=t, POHDate=q.POHDate, Section=y)
            newDef.save()
            print(newDef)
            print(newDef.TCName)
            print(newDef.TCDefArea)
            print(newDef.TCDef)
            message = messages.success(request, "TC Deficiency Record  Added: {} --> {} --> {} ".format(newDef.TCName,newDef.TCDefArea,newDef.TCDef))
        else:
            message = messages.warning(request, "TC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-POHDate')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)


@login_required
def addMCpart(request, Serial):
    q = MC.objects.get(id=Serial)
    if MCArea.objects.filter(MCArea=request.POST.get('addMCpart')).exists():
        message = messages.warning(request, "MC Part already exists ")
        p = MCRemark.objects.filter(MCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/mcdefdet.html', context)
        pass
    if request.method == 'POST':
        newPart = MCArea(MCArea=request.POST.get('addMCpart'))
        newPart.save()
        print(newPart)
        message = messages.success(request, "MC Part '{}' Added ".format(newPart))
    else:
        message = messages.warning(request, "MC Part Not Added ")
    p = MCRemark.objects.filter(MCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)

@login_required
def addMCdef(request, Serial):
    q = MC.objects.get(id=Serial)
    if MCDef.objects.filter(MCDef=request.POST.get('addMCdef')).exists():
        message = messages.warning(request, "MC Deficiency already exists ")
        p = MCRemark.objects.filter(MCName=q.id).order_by('-POHDate')
        context = {
        #'messages': message,
        'object': q,
        'q' : p,
        'message' : message,
            }
        return render(request, 'deficiencies/mcdefdet.html', context)
        pass
    if request.method == 'POST':
        newDef = MCDef(MCDef=request.POST.get('addMCdef'))
        newDef.save()
        print(newDef)
        message = messages.success(request, "MC Deficiency '{}' Added ".format(newDef))
    else:
        message = messages.warning(request, "MC Deficiency Not Added ")
    p = MCRemark.objects.filter(MCName=q.id).order_by('-POHDate')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)


@login_required
def addMCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def') and request.POST.get('Section'):
        q = MC.objects.filter(id=Serial).first()
        r = MCArea.objects.filter(MCArea=request.POST.get('Part')).first()
        t = MCDef.objects.filter(MCDef=request.POST.get('Def')).first()
        y = MCSection.objects.filter(Section=request.POST.get('Section')).first()
        if request.method == 'POST':
            newDef = MCRemark(MCName=q, MCDefArea=r, MCDef=t, POHDate=q.POHDate, Section=y)
            newDef.save()
            print(newDef)
            print(newDef.MCName)
            print(newDef.MCDefArea)
            print(newDef.MCDef)
            message = messages.success(request, "MC Deficiency Record  Added: {} --> {} --> {} ".format(newDef.MCName, newDef.MCDefArea,newDef.MCDef))
        else:
            message = messages.warning(request, "MC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-POHDate')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def partAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(DPCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.DPCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')

@login_required
def defAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCDef.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(DPCDef__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.DPCDef
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')

@login_required
def SecAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCSection.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Section__icontains=itemTerm).exclude(Section="Default")
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Section
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/dpcdefdet.html')


@login_required
def TCpartAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = TCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(TCCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.TCCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/tcdefdet.html')

@login_required
def TCdefAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = TCDef.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(TCDef__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.TCDef
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/tcdefdet.html')

@login_required
def TCSecAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = TCSection.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Section__icontains=itemTerm).exclude(Section="Default")
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Section
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/tcdefdet.html')


@login_required
def MCpartAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MCArea.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(MCArea__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.MCArea
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/mcdefdet.html')

@login_required
def MCdefAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MCDef.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(MCDef__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.MCDef
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/mcdefdet.html')

@login_required
def MCSecAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MCSection.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Section__icontains=itemTerm).exclude(Section="Default")
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Section
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'deficiencies/mcdefdet.html')


@login_required
def DefiListHome2(request):
    dpc = DPC.objects.all().order_by('-POHDate')
    tc = TC.objects.all().order_by('-POHDate')
    mc = MC.objects.all().order_by('-POHDate')
        
        
    context = {
            'dpc': dpc,
            'tc' : tc,
            'mc' : mc,
    }
    print('successful')
    return render(request, 'deficiencies/deflisthome.html', context)


@login_required
def DTMpartAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCArea.objects.all()
            qs2 = TCArea.objects.all()
            qs3 = MCArea.objects.all()
            itemTerm = request.GET.get('term')
            list2 = {"label":[], "category":[]}
            list3 = {"label":[], "category":[]}
            list4 = list()
            res = qs.filter(DPCArea__icontains=itemTerm)
            print(res)
            if res:
                for q in res:
                    list1 = {"label":[], "category":'DPC'}
                    list1["label"].append(f'DPC-{q.DPCArea}')
                    list4.append(list1)
            res2 = qs2.filter(TCCArea__icontains=itemTerm)
            if res2:
                for q in res2:
                    list2 = {"label":[], "category":'TC'}
                    list2["label"].append(f'TC-{q.TCCArea}')
                    list4.append(list2)
            res3 = qs3.filter(MCArea__icontains=itemTerm)
            if res3:
                for q in res3:
                    list3 = {"label":[], "category":'MC'}
                    list3["label"].append(f'MC-{q.MCArea}')
                    list4.append(list3)
            print("list4")
            print(list4)
            return JsonResponse(list4, safe=False)

            return render(request, 'deficiencies/deflisthome.html')


@login_required
def DTMsectionAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = DPCSection.objects.all()
            qs2 = TCSection.objects.all()
            qs3 = MCSection.objects.all()
            itemTerm = request.GET.get('term')
            list2 = {"label":[], "category":[]}
            list3 = {"label":[], "category":[]}
            list4 = list()
            res = qs.filter(Section__icontains=itemTerm).exclude(Section="Default")
            print(res)
            if res:
                for q in res:
                    list1 = {"label":[], "category":'DPC'}
                    list1["label"].append(f'DPC-{q.Section}')
                    list4.append(list1)
            res2 = qs2.filter(Section__icontains=itemTerm).exclude(Section="Default")
            if res2:
                for q in res2:
                    list2 = {"label":[], "category":'TC'}
                    list2["label"].append(f'TC-{q.Section}')
                    list4.append(list2)
            res3 = qs3.filter(Section__icontains=itemTerm).exclude(Section="Default")
            if res3:
                for q in res3:
                    list3 = {"label":[], "category":'MC'}
                    list3["label"].append(f'MC-{q.Section}')
                    list4.append(list3)
            print("list4")
            print(list4)
            return JsonResponse(list4, safe=False)

            return render(request, 'deficiencies/deflisthome.html')


@login_required
def DTMsearch(request):
    list1 = []
    list2 = []
    if request.POST:
        if request.POST.get('datepicker') and request.POST.get('datepicker1'):
            if request.POST.get('Part') and not request.POST.get('Section'):
                q = request.POST.get('Part')
                if q.startswith("DPC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = DPCArea.objects.all().filter(DPCArea__icontains=r[0])
                    w = DPCRemark.objects.all().order_by("-POHDate").filter(DPCDefArea=t[0].id)
                    for x in w:
                        list1.append(x)
                    message = messages.success(request, f"Search for {request.POST.get('Part')} complete.")
                elif q.startswith("TC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = TCArea.objects.all().filter(TCCArea__icontains=r[0])
                    w = TCRemark.objects.all().order_by("-POHDate").filter(TCDefArea=t[0].id)
                    for x in w:
                        list1.append(x)
                        print(list1)
                    message = messages.success(request, f"Search for {request.POST.get('Part')} complete.")
                elif q.startswith("MC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = MCArea.objects.all().filter(MCArea__icontains=r[0])
                    w = MCRemark.objects.all().order_by("-POHDate").filter(MCDefArea=t[0].id)
                    for x in w:
                        list1.append(x)
                    message = messages.success(request, f"Search for {request.POST.get('Part')} complete.")
                else:
                    message = messages.warning(request, "Not a valid search")
            elif request.POST.get('Section') and not request.POST.get('Part'):
                q = request.POST.get('Section')
                if q.startswith("DPC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = DPCSection.objects.all().filter(Section__icontains=r[0])
                    w = DPCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    for x in w:
                        list2.append(x)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} complete.")
                elif q.startswith("TC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = TCSection.objects.all().filter(Section__icontains=r[0])
                    w = TCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    for x in w:
                        list2.append(x)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} complete.")
                elif q.startswith("MC-"):
                    r = q.split("-")
                    r.pop(0)
                    t = MCSection.objects.all().filter(Section__icontains=r[0])
                    w = MCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    for x in w:
                        list2.append(x)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} complete.")
                else:
                    message = messages.warning(request, "Not a valid search")
            elif request.POST.get('Section') and request.POST.get('Part'):
                q = request.POST.get('Section')
                d = request.POST.get('Part')
                if q.startswith("DPC-") and d.startswith("DPC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = DPCSection.objects.all().filter(Section__icontains=r[0])
                    g = DPCArea.objects.all().filter(DPCArea__icontains=u[0])
                    w = DPCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = DPCRemark.objects.all().order_by("-POHDate").filter(DPCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("TC-") and d.startswith("TC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = TCSection.objects.all().filter(Section__icontains=r[0])
                    g = TCArea.objects.all().filter(TCCArea__icontains=u[0])
                    w = TCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = TCRemark.objects.all().order_by("-POHDate").filter(TCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("MC-") and d.startswith("MC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = MCSection.objects.all().filter(Section__icontains=r[0])
                    g = MCArea.objects.all().filter(MCArea__icontains=u[0])
                    w = MCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = MCRemark.objects.all().order_by("-POHDate").filter(MCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("DPC-") and d.startswith("TC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = DPCSection.objects.all().filter(Section__icontains=r[0])
                    g = TCArea.objects.all().filter(TCCArea__icontains=u[0])
                    w = DPCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = TCRemark.objects.all().order_by("-POHDate").filter(TCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("TC-") and d.startswith("MC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = TCSection.objects.all().filter(Section__icontains=r[0])
                    g = MCArea.objects.all().filter(MCArea__icontains=u[0])
                    w = TCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = MCRemark.objects.all().order_by("-POHDate").filter(MCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("MC-") and d.startswith("DPC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = MCSection.objects.all().filter(Section__icontains=r[0])
                    g = DPCArea.objects.all().filter(DPCArea__icontains=u[0])
                    w = MCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = DPCRemark.objects.all().order_by("-POHDate").filter(DPCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("DPC-") and d.startswith("MC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = DPCSection.objects.all().filter(Section__icontains=r[0])
                    g = MCArea.objects.all().filter(MCArea__icontains=u[0])
                    w = DPCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = MCRemark.objects.all().order_by("-POHDate").filter(MCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("TC-") and d.startswith("DPC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = TCSection.objects.all().filter(Section__icontains=r[0])
                    g = DPCArea.objects.all().filter(DPCArea__icontains=u[0])
                    w = TCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = DPCRemark.objects.all().order_by("-POHDate").filter(DPCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                elif q.startswith("MC-") and d.startswith("TC-"):
                    r = q.split("-")
                    u = d.split("-")
                    r.pop(0)
                    u.pop(0)
                    t = MCSection.objects.all().filter(Section__icontains=r[0])
                    g = TCArea.objects.all().filter(TCCArea__icontains=u[0])
                    w = MCRemark.objects.all().order_by("-POHDate").filter(Section=t[0].id)
                    y = TCRemark.objects.all().order_by("-POHDate").filter(TCDefArea=g[0].id)
                    for x in w:
                        list2.append(x)
                    for xm in y:
                        list1.append(xm)
                    message = messages.success(request, f"Search for {request.POST.get('Section')} & {request.POST.get('Part')} complete.")
                else:
                    message = messages.warning(request, "Not a valid search")
            else:
                message = messages.warning(request, "Please select a part and/or section")
        else:
            message = messages.warning(request, "Please Enter Dates")

    print("*******************")
    print(list1)
    print(list2)
    context = {
        'part': list1,
        'section': list2,
        'partname': request.POST.get('Part'),
        'sectionname': request.POST.get('Section'),
        }


    return render(request, 'deficiencies/deflisthome.html', context)