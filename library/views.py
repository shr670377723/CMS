from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.models import *


def bookInfo(request):
    if request.method == 'GET':
        return render(request,'bookInfo.html')
    else:
        # print(request.POST.dict())
        sh = request.POST.get('bid')
        sm = request.POST.get('bname')
        zz = request.POST.get('author')
        lb = request.POST.get('category')
        cbs = request.POST.get('publication')
        fxrq = request.POST.get('pubdate')
        czy = request.POST.get('operator')
        jg = request.POST.get('price')
        rksl = request.POST.get('bnum')
        rksj = request.POST.get('indate')
        tsjj = request.POST.get('intro')
        many = (sh,sm,zz,lb,cbs,fxrq,czy,jg,rksj,rksl,tsjj)
        # print(many)
        # for a in many:
        #     print(a+'-')
        l=[1,'',2]
        print(len(l))
        try:
                #     print('1')
                # else:
                #     # ('', '', '', '', '', '', '', '', '', '', '')
                #     return render(request, 'file.html')
            try :
               bk = Bookinfo.objects.get(bid=sh,bname=sm,author=zz,category=lb,publication=cbs,pubdate=fxrq,bnum=rksl,indate=rksj,price=jg,intro=tsjj,operator=czy)
            except:
               bk = Bookinfo.objects.create(bid=sh,bname=sm,author=zz,category=lb,publication=cbs,pubdate=fxrq,bnum=rksl,indate=rksj,price=jg,intro=tsjj,operator=czy)
                # bk.save()
            return render(request,'ok.html')
        except:
            return HttpResponse('不能为空')

def bookMaintain(request):
    return render(request,'bookMaintain.html')
import datetime
def bookBorrow(request):
    if request.method == "GET":
        # borrow = Bookborrow.objects.all()
        return render(request,'bookBorrow.html')
    else:
        xh =  request.POST.get('sid')
        # xm =  request.POST.get('sname')
        sh =  request.POST.get('bid')
        sm =  request.POST.get('bname')
        jyrq=  request.POST.get('borrowdate')
        czy =  request.POST.get('operator')
        returndate = datetime.datetime.now()
        all = (xh,sh,jyrq,czy)
        try:
            b = Bookinfo.objects.get(bid=sh)
            x = Admissionsforms.objects.get(sid=xh)
            stu = Stuinfo.objects.get(sid=x)
            Bookborrow.objects.create(sid=stu,borrowdate=jyrq,operator=czy,bid=b,returndate=returndate)
            borrow = Bookborrow.objects.filter(borrowdate=jyrq,bid__bname=sm,operator=czy)
            return render(request, 'bookBorrow.html',{'borrow':borrow})
        except:
            return HttpResponse('不能为空')

def bookReturn(request):
    if request.method == 'GET':
        borrow = Bookborrow.objects.all()
        return render(request,'bookReturn.html',{'borrow':borrow})
    else:
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        bid = request.POST.get('bid')
        bname = request.POST.get('bname')
        borrowdate = request.POST.get('borrowdate')
        many = (sid,sname,bid,bname,borrowdate)
        try:
            Bookborrow.objects.filter(bid=bid,sid=sid,bid__bname=bname,sid__sid__sname=sname,borrowdate=borrowdate).delete()
            borrow = Bookborrow.objects.all()
            return render(request, 'bookReturn.html',{'borrow':borrow})
        except:
            return HttpResponse('字段不能为空')


def borrowQuery(request):
    if request.method == 'GET':
        return render(request,'borrowQuery.html')
    else:
        select = request.POST.get('select')
        al = request.POST.get('all')
        # print(select,al)
        if select == 'xh':
            cx = Bookborrow.objects.filter(sid=al)
            # print(cx)
        elif select == 'sh':
            cx = Bookborrow.objects.filter(bid=al)
            # print(cx)
        elif select == 'jyrq':
            cx = Bookborrow.objects.filter(borrowdate=al)
        return render(request,'borrowQuery.html',{'cx':cx})