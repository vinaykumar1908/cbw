from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import datetime
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import ModuleRecievedForm, ModuleDefectForm
from django.db.models import Q
#from sidingz.models import ModuleRecieved
from defi.models import DPCRemark, TCRemark, MCRemark, DPC, TC, MC, DPCArea, TCArea, MCArea
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
def LetterView(request):
    
    return render(request, 'letters/confidentialframe.html')

def LetterPrintPdf(request):
    
    
    To = request.POST.get('To')
    LNo = request.POST.get('LNo')
    date = request.POST.get('datepicker1')
    Designation = request.POST.get('Designation')
    Address = request.POST.get('Address')
    subject = request.POST.get('subject')
    matter = request.POST.get('matter')
    cc1 = request.POST.get('cc1')
    cc2 = request.POST.get('cc2')
    cc3 = request.POST.get('cc3')
    cc4 = request.POST.get('cc4')
    rolstock = request.POST.get('RolStock')
    part = request.POST.get('part')
    
    
    list1 = []
    listq = []
    daterange = ()
    if request.POST.get('RolStock'):
        f = rolstock.split(',')
        for x in f:
            if x.startswith("DPC-"):
                d = DPC.objects.all().order_by('-POHDate').filter(DPCName=x).first()
                e = f'{d}. POH {d.POHDate}'
                print("****************")
                print(d)
                c =  DPCRemark.objects.all().order_by('-POHDate').filter(DPCName=d.id)
                list2 = []
                for x in c:
                    v = str(x.DPCDef)
                    w = str(x.DPCDefArea)
                    list2.append(f'{w}. {v}')   
                print(c)
                t = {e:list2}
                list1.append(t)
                print(list1)
            elif x.startswith("TC-"):
                d = TC.objects.all().order_by('-POHDate').filter(TCName=x).first()
                e = str(TC.objects.all().order_by('-POHDate').filter(TCName=x).first())
                print("****************")
                print(d)
                c =  TCRemark.objects.all().order_by('-POHDate').filter(TCName=d.id)
                list2 = []
                for x in c:
                    v = str(x.TCDef)
                    w = str(x.TCDefArea)
                    list2.append(f'{w}. {v}')   
                print(c)
                t = {e:list2}
                list1.append(t)
                print(list1)
            elif x.startswith("MC-"):
                d = MC.objects.all().order_by('-POHDate').filter(MCName=x).first()
                e = str(MC.objects.all().order_by('-POHDate').filter(MCName=x).first())
                print("****************")
                print(d)
                c =  MCRemark.objects.all().order_by('-POHDate').filter(MCName=d.id)
                list2 = []
                for x in c:
                    v = str(x.MCDef)
                    w = str(x.MCDefArea)
                    list2.append(f'{w}. {v}')   
                print(c)
                t = {e:list2}
                list1.append(t)
                print(list1)
            else:
                print("Not a Sanctioned Car")
                print(x)
        print("****************")
        print(list1)
    if request.POST.get('part') and request.POST.get('datepicker3') and request.POST.get('datepicker4'):
        Part = request.POST.get('part')
        Part = Part.split(',')
        print(Part)
        listq = []
        for x in Part:
            if DPCArea.objects.all().filter(DPCArea=x).first():
                q = DPCArea.objects.all().get(DPCArea=x)
                w = DPCRemark.objects.all().order_by("-POHDate").filter(DPCDefArea=q.id).filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
                a = []
                for s in w:
                    a.append(str(s.DPCName))
                newline = '\n'
                listq.append({q:(f'DPC part {q} has {w.count()} case/s in car/s{newline}{newline.join(a)}.')})
            if TCArea.objects.all().filter(TCCArea=x).first():
                e = TCArea.objects.all().get(TCCArea=x)
                r = TCRemark.objects.all().order_by("-POHDate").filter(TCDefArea=e.id).filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
                a = []
                for s in r:
                    a.append(str(s.TCName))
                newline = '\n'
                listq.append({q:(f'TC part {e} has {r.count()} case/s in car/s{newline}{newline.join(a)}.')})
            if MCArea.objects.all().filter(MCArea=x).first():
                t = MCArea.objects.all().filter(MCArea=x).first()
                y = MCRemark.objects.all().order_by("-POHDate").filter(MCDefArea=t.id).filter(POHDate__lt=request.POST.get('datepicker4'), POHDate__gt=request.POST.get('datepicker3'))
                a = []
                for s in y:
                    a.append(str(s.MCName))
                newline = '\n'
                listq.append({t:(f'MC part {t} has {y.count()} case/s in car/s{newline}{newline.join(a)}.')})
        print(listq)
        f = request.POST.get('datepicker3')
        g = request.POST.get('datepicker4')
        daterange = (f'{f} to {g}')
    if date == '':
        date = datetime. datetime. now(). date()
    template_path = 'letters/confidentialpdf.html'
    user = request.user
    context = {
        'date' : date,
        'To' : To,
        'Designation' : Designation,
        'Address' : Address,
        'subject' : subject,
        'matter' : matter,
        'cc1' : cc1,
        'cc2' : cc2,
        'cc3' : cc3,
        'cc4' : cc4,
        'user' : user,
        'data' : list1,
        'rolstock': request.POST.get('RolStock'),
        'data2' : listq,
        'Part' : request.POST.get('part'),
        'LNo' : request.POST.get('LNo'),
        'daterange' : daterange,
    }
    print(date)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
