from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from mnp.models import MNPShop, MNPSection, MNPType, MnP, MnPRemark
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.


@login_required
def addData(request):
    mnp = []
    list1 = []
    
    mnp = MnP.objects.all().order_by('-UpdateDate')
    mnpShop = MNPShop.objects.all().order_by('Date').exclude(Shop='Default')
    mnpSection = MNPSection.objects.all().order_by('-Date')
    for x in mnpShop:
        r = mnpSection.filter(Shop=x)
        print(x)
        print(r)
        list2 = []
        for c in r:
            t = mnp.filter(Section=c)
            list2.append({c.Section:t})
            print(c)
            print(list2)
        list1.append({x.Shop:list2})
    print('list1')
    print(list1)

    
        
        
    context = {
             'mnp': list1,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/addMnpData.html', context)


@login_required
def status(request):
    # dpc = DPC0.objects.all().order_by('-POHDate')
    # tc = TC0.objects.all().order_by('-POHDate')
    # mc = MC0.objects.all().order_by('-POHDate')
        
        
    context = {
            # 'dpc': dpc,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/MnpStatus.html', context)


@login_required
def AddMnp(request):
    data = []
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("Shop") and request.POST.get("Section") and request.POST.get("MachineName") and request.POST.get("Type"):
            if MNPShop.objects.all().filter(Shop=request.POST.get("Shop")).exists():
                data.append(f'all details filled Shop {request.POST.get("Shop")} !')
                if MNPSection.objects.all().filter(Section=request.POST.get("Section")).exists():
                    data.append(f'all details filled Section {request.POST.get("Section")} !')
                    if MNPType.objects.all().filter(Type=request.POST.get("Type")).exists():
                        data.append(f'all details filled Type {request.POST.get("Type")}!')
                        q = MNPShop.objects.get(Shop=request.POST.get("Shop"))
                        w = MNPSection.objects.get(Section=request.POST.get("Section"))
                        e = MNPType.objects.get(Type=request.POST.get("Type"))
                        newMNP = MnP(MachineName=request.POST.get("MachineName"),Shop=q,Section=w,Type=e,author=request.user)
                        print(newMNP)
                        newMNP.save()
                    else:
                        data.append(f'No such Type')
                else:
                    data.append(f'No such Section')
            else:
                data.append(f'No such Shop')
        else:
            data = f'All details not added'

    mnp = []
    list1 = []
    
    mnp = MnP.objects.all().order_by('-UpdateDate')
    mnpShop = MNPShop.objects.all().order_by('Date').exclude(Shop='Default')
    mnpSection = MNPSection.objects.all().order_by('-Date')
    for x in mnpShop:
        r = mnpSection.filter(Shop=x)
        print(x)
        print(r)
        list2 = []
        for c in r:
            t = mnp.filter(Section=c)
            list2.append({c.Section:t})
            print(c)
            print(list2)
        list1.append({x.Shop:list2})
    print('list1')
    print(list1)


    context = {
        'mnp' : list1,
            # 'dpc': dpc,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/addMnpData.html', context)

@login_required
def showmnpdet(request, Serial):
    print("--------------------**------------------")
    p = MnP.objects.get(id=Serial)
    q = MnPRemark.objects.filter(MachineName=p.id).order_by('-created_date')
    print(p)
    print(q)
    context = {
        'p' : p,
        'q': q,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/mnpdetail.html', context)

@login_required
def AddMnpRemark(request, Serial):
    print("--------------------**------------------")
    p = MnP.objects.get(id=Serial)
    print(request.POST)
    print(request.FILES)
    print(p)
    filepath = request.FILES.get('myfile', False)
    if request.method == 'POST' and filepath != False:
        print("1--------------------**------------------")
        newRemark = MnPRemark(MachineName=p,author=request.user, text=request.POST.get('matter'), commentfile=filepath)
        newRemark.save()
    else:
        newRemark = MnPRemark(MachineName=p,author=request.user, text=request.POST.get('matter'))
        newRemark.save()
    q = MnPRemark.objects.filter(MachineName=p.id).order_by('-created_date')
    print(p)
    print(q)
    context = {
        'p' : p,
        'q': q,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/mnpdetail.html', context)



@login_required
def togglestatus(request,Serial):
    p = MnP.objects.get(id=Serial)
    if p.MnPStatus == True:
        p.MnPStatus = False
        print("*****MnPTrueStatus****")
        print(p.MnPStatus)
        p.save()
    elif p.MnPStatus == False:
        p.MnPStatus = True
        print("*****MnPFalseStatus****")
        print(p.MnPStatus)
        p.save()
    print(p)
    q = MnPRemark.objects.filter(MachineName=p.id).order_by('-created_date')
    print(p)
    print(q)
    context = {
        'p' : p,
        'q': q,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/mnpdetail.html', context)


@login_required
def ShopAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MNPShop.objects.all().exclude(Shop='Default')
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Shop__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Shop
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'mnp/addMnpData.html')

@login_required
def SectionAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MNPSection.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Section__icontains=itemTerm)
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

            return render(request, 'mnp/addMnpData.html')

@login_required
def TypeAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MNPType.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(Type__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.Type
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'mnp/addMnpData.html')