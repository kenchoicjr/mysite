from django.contrib import admin
from django.conf.urls import url, include
import zqfx.views

app_name = 'zqfx'

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', customerservice.views.weixin_main),
    url(r'zqfx/', zqfx.views.zqfx),
    url(r'win007/', zqfx.views.win007),
    url(r'vipc/', zqfx.views.vipc),
    url(r'leisu/', zqfx.views.leisu),
    url(r'tipc/', zqfx.views.tipc),
    url(r'all_list/', zqfx.views.all_list),
]
