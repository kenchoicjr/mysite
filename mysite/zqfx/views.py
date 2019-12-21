from django.shortcuts import render
from zqfx.models import Win007, Zqfx, Vipc,Leisu,Tips,AllInfoOrm
# from zqfx.mysql_view_models import AllInfoOrm
import datetime


def zqfx(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    zqfxs = Zqfx.objects.filter(datec=d)
    context = {'zqfxs': zqfxs}
    # print(zqfxs)
    return render(request, 'zqfx/zqfx.html', context)


def win007(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    win007s = Win007.objects.filter(datec=d).order_by('cc')
    context = {'win007s': win007s}
    print(win007s)
    return render(request, 'zqfx/win007.html', context)


def vipc(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    vipcs = Vipc.objects.filter(datec=d).order_by('cc')
    context = {'vipcs': vipcs}
    # print(vipc)
    return render(request, 'zqfx/vipc.html', context)


def leisu(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    leisus = Leisu.objects.filter(datec=d).order_by('cc')
    context = {'leisus': leisus}
    # print(leisu)
    return render(request, 'zqfx/leisu.html', context)


def tipc(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    tipcs = Tips.objects.filter(datec=d).order_by('cc')
    # zqfxs = Zqfx.objects.filter(datec=d)
    context = {'tipcs': tipcs}
    # print(leisu)
    return render(request, 'zqfx/tipc.html', context)


def all_list(request):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    d2=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=-1),
                               '%Y%m%d')
    all_list = AllInfoOrm.objects.filter(datec=d).order_by('cc')
    # zqfxs = Zqfx.objects.filter(datec=d)
    # print(all_list)
    context = {'all_list': all_list}
    # print(leisu)
    return render(request, 'zqfx/all_list.html', context)


