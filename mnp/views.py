from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from mnp.models import MNPShop, MNPSection, MNPType, MnP, MnPRemark
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


@login_required
def addData(request):
    # dpc = DPC0.objects.all().order_by('-POHDate')
    # tc = TC0.objects.all().order_by('-POHDate')
    # mc = MC0.objects.all().order_by('-POHDate')
        
        
    context = {
            # 'dpc': dpc,
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
    if request.method == 'POST':
        print(request.POST)



    context = {
            # 'dpc': dpc,
            # 'tc' : tc,
            # 'mc' : mc,
    }
    print('successful')
    return render(request, 'mnp/addMnpData.html', context)

@login_required
def ShopAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = MNPShop.objects.all()
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