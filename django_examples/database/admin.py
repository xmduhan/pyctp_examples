# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from models import *

class DepthMarketDataAdmin(admin.ModelAdmin):
    """
    行情数据编辑显示定义
    """
    fields = [i.name for i in ModelDepthMarketData._meta.fields[1:]]

admin.site.register(ModelDepthMarketData,DepthMarketDataAdmin)
