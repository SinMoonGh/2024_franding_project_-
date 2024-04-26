from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic import FormView

from django.db.models import Q
from .models import *
# Create your views here.

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list_item(request):
    items = Item.objects.all()
    paginator = Paginator(items, 4)  # 한 페이지에 20개씩 표시
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'items': page_obj,
        'cat1': Category1.objects.all(),
        'cat2': Category2.objects.all(),
    }
    return render(request, 'item/list.html', context)




#category 정리
#100번대->cat1
#200번대->cat2
#250번대->detail_cat2
#300번대->brand
#400번대->item_type
def cat_list_item(request,cat_id):
    if int(cat_id)>100 and int(cat_id)<200:
        cat_id = cat_id-100
        cat = Category1.objects.get(id=cat_id)
        #아이템 모델에서 카테고리 1 값이 cat과 동일한 데이터를 찾아서 반환
        context={
        "key":Item.objects.filter(cat1 = cat)
        } #리퀘스트, 템플릿주소, 콘텍스트 를 반환
        return render(request,'item/cat_list.html',context)
    elif int(cat_id)>200 and int(cat_id)<300:
        cat_id = cat_id-200
        cat= Category2.objects.get(id=cat_id)
        context={
        "key":Item.objects.filter(cat2 = cat)
        }
        return render(request,'item/cat_list.html',context)
    elif int(cat_id)==300:
        cat = Item.objects.all()
        context={
        "key":cat
        }
        return render(request,'item/cat_list.html',context)
    elif int(cat_id)>300 and int(cat_id)<400:
        cat_id = cat_id-300
        cat = Brand.objects.get(id=cat_id)
        context={
        "key":Item.objects.filter(brand = cat)
        }
        return render(request,'item/cat_list.html',context)
    elif int(cat_id)>400 and int(cat_id)<500:
        cat_id = cat_id-400
        cat = ItemType.objects.get(id=cat_id)
        context={
        "key":Item.objects.filter(item_type = cat)
        }
        return render(request,'item/cat_list.html',context)
def detail_list_item(request,item_id):
    model=Item.objects.get(id=item_id)
    context={
        "item":model
    }
    return render(request,'item/detail.html',context)
