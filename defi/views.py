from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import DPC, TC, MC, DPCArea, DPCDef, DPCRemark, TCArea, TCDef, TCRemark, MCArea, MCDef, MCRemark
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.



class DefiHome(LoginRequiredMixin, TemplateView):
    template_name = 'deficiencies/defhome.html'



@login_required
def DefiHome2(request):
    dpc = DPC.objects.all().order_by('-Date')
    tc = TC.objects.all().order_by('-Date')
    mc = MC.objects.all().order_by('-Date')
        
        
    context = {
            'dpc': dpc,
            'tc' : tc,
            'mc' : mc,
    }
    print('successful')
    return render(request, 'deficiencies/defhome.html', context)

@login_required
def AddDPC(request):
    if request.method == 'POST' and request.POST.get('DPCNum').startswith("DPC"):
        newDPC = DPC(DPCName=request.POST.get('DPCNum'),author=request.user)
        newDPC.save()
        message = messages.success(request, "DPC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        tc = TC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
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
        dpc = DPC.objects.all().order_by('-Date')
        tc = TC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    

@login_required
def AddTC(request):
    if request.method == 'POST' and request.POST.get('TCNum').startswith("TC"):
        newTC = TC(TCName=request.POST.get('TCNum'),author=request.user)
        newTC.save()
        message = messages.success(request, "TC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        tc = TC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
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
        dpc = DPC.objects.all().order_by('-Date')
        tc = TC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
        context = {
                'dpc': dpc,
                'tc' : tc,
                'mc' : mc,
                
                'message' : message,
            }
    return render(request, 'deficiencies/defhome.html', context)
    
@login_required
def AddMC(request):
    if request.method == 'POST' and request.POST.get('MCNum').startswith("MC"):
        newMC = MC(MCName=request.POST.get('MCNum'),author=request.user)
        newMC.save()
        message = messages.success(request, "MC Added ")
        dpc = DPC.objects.all().order_by('-Date')
        tc = TC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
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
        dpc = DPC.objects.all().order_by('-Date')
        mc = MC.objects.all().order_by('-Date')
        
        
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
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-Date')
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
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
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
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
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
        p = DPCRemark.objects.filter(DPCName=q.id).order_by('-Date')
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
        message = messages.success(request, "DPC Part  Added ")
    else:
        message = messages.warning(request, "DPC Part Not Added ")
    p = DPCRemark.objects.filter(DPCName=q.id).order_by('-Date')
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
        p = DPCRemark.objects.filter(DPCName=q.id).order_by('-Date')
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
        message = messages.success(request, "DPC Deficiency  Added ")
    else:
        message = messages.warning(request, "DPC Deficiency Not Added ")
    p = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/dpcdefdet.html', context)


@login_required
def addDPCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def'):
        q = DPC.objects.filter(id=Serial).first()
        r = DPCArea.objects.filter(DPCArea=request.POST.get('Part')).first()
        t = DPCDef.objects.filter(DPCDef=request.POST.get('Def')).first()
        if request.method == 'POST':
            newDef = DPCRemark(DPCName=q, DPCDefArea=r, DPCDef=t)
            newDef.save()
            print(newDef)
            print(newDef.DPCName)
            print(newDef.DPCDefArea)
            print(newDef.DPCDef)
            message = messages.success(request, "DPC Deficiency Record  Added ")
        else:
            message = messages.warning(request, "DPC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill Both Entries ")

    
    p = DPC.objects.get(id=Serial)
    q = DPCRemark.objects.filter(DPCName=p.id).order_by('-Date')
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
        p = TCRemark.objects.filter(TCName=q.id).order_by('-Date')
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
        message = messages.success(request, "TC Part  Added ")
    else:
        message = messages.warning(request, "TC Part Not Added ")
    p = TCRemark.objects.filter(TCName=q.id).order_by('-Date')
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
        p = TCRemark.objects.filter(TCName=q.id).order_by('-Date')
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
        message = messages.success(request, "TC Deficiency  Added ")
    else:
        message = messages.warning(request, "TC Deficiency Not Added ")
    p = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/tcdefdet.html', context)


@login_required
def addTCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def'):
        q = TC.objects.filter(id=Serial).first()
        r = TCArea.objects.filter(TCCArea=request.POST.get('Part')).first()
        t = TCDef.objects.filter(TCDef=request.POST.get('Def')).first()
        if request.method == 'POST':
            newDef = TCRemark(TCName=q, TCDefArea=r, TCDef=t)
            newDef.save()
            print(newDef)
            print(newDef.TCName)
            print(newDef.TCDefArea)
            print(newDef.TCDef)
            message = messages.success(request, "TC Deficiency Record  Added ")
        else:
            message = messages.warning(request, "TC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill Both Entries ")

    
    p = TC.objects.get(id=Serial)
    q = TCRemark.objects.filter(TCName=p.id).order_by('-Date')
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
        p = MCRemark.objects.filter(MCName=q.id).order_by('-Date')
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
        message = messages.success(request, "MC Part  Added ")
    else:
        message = messages.warning(request, "MC Part Not Added ")
    p = MCRemark.objects.filter(MCName=q.id).order_by('-Date')
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
        p = MCRemark.objects.filter(MCName=q.id).order_by('-Date')
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
        message = messages.success(request, "MC Deficiency  Added ")
    else:
        message = messages.warning(request, "MC Deficiency Not Added ")
    p = MCRemark.objects.filter(MCName=q.id).order_by('-Date')
    context = {
        #'messages': message,
        'object': q,
        'q' : p,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)


@login_required
def addMCRemark(request, Serial):
    if request.POST.get('Part') and request.POST.get('Def'):
        q = MC.objects.filter(id=Serial).first()
        r = MCArea.objects.filter(MCArea=request.POST.get('Part')).first()
        t = MCDef.objects.filter(MCDef=request.POST.get('Def')).first()
        if request.method == 'POST':
            newDef = MCRemark(MCName=q, MCDefArea=r, MCDef=t)
            newDef.save()
            print(newDef)
            print(newDef.MCName)
            print(newDef.MCDefArea)
            print(newDef.MCDef)
            message = messages.success(request, "MC Deficiency Record  Added ")
        else:
            message = messages.warning(request, "MC Deficiency Record Not Added ")
    else:
        message = messages.warning(request, "Please Fill Both Entries ")

    
    p = MC.objects.get(id=Serial)
    q = MCRemark.objects.filter(MCName=p.id).order_by('-Date')
    print(q)
    context = {
        #'messages': message,
        'object': p,
        'q' : q,
    }
    return render(request, 'deficiencies/mcdefdet.html', context)


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