# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelDepthMarketData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TradingDay', models.CharField(default=b'', max_length=9, verbose_name='\u4ea4\u6613\u65e5')),
                ('InstrumentID', models.CharField(default=b'', max_length=31, verbose_name='\u5408\u7ea6\u4ee3\u7801')),
                ('ExchangeID', models.CharField(default=b'', max_length=9, verbose_name='\u4ea4\u6613\u6240\u4ee3\u7801')),
                ('ExchangeInstID', models.CharField(default=b'', max_length=31, verbose_name='\u5408\u7ea6\u5728\u4ea4\u6613\u6240\u7684\u4ee3\u7801')),
                ('LastPrice', models.FloatField(default=0, verbose_name='\u6700\u65b0\u4ef7')),
                ('PreSettlementPrice', models.FloatField(default=0, verbose_name='\u4e0a\u6b21\u7ed3\u7b97\u4ef7')),
                ('PreClosePrice', models.FloatField(default=0, verbose_name='\u6628\u6536\u76d8')),
                ('PreOpenInterest', models.FloatField(default=0, verbose_name='\u6628\u6301\u4ed3\u91cf')),
                ('OpenPrice', models.FloatField(default=0, verbose_name='\u4eca\u5f00\u76d8')),
                ('HighestPrice', models.FloatField(default=0, verbose_name='\u6700\u9ad8\u4ef7')),
                ('LowestPrice', models.FloatField(default=0, verbose_name='\u6700\u4f4e\u4ef7')),
                ('Volume', models.IntegerField(default=0, verbose_name='\u6570\u91cf')),
                ('Turnover', models.FloatField(default=0, verbose_name='\u6210\u4ea4\u91d1\u989d')),
                ('OpenInterest', models.FloatField(default=0, verbose_name='\u6301\u4ed3\u91cf')),
                ('ClosePrice', models.FloatField(default=0, verbose_name='\u4eca\u6536\u76d8')),
                ('SettlementPrice', models.FloatField(default=0, verbose_name='\u672c\u6b21\u7ed3\u7b97\u4ef7')),
                ('UpperLimitPrice', models.FloatField(default=0, verbose_name='\u6da8\u505c\u677f\u4ef7')),
                ('LowerLimitPrice', models.FloatField(default=0, verbose_name='\u8dcc\u505c\u677f\u4ef7')),
                ('PreDelta', models.FloatField(default=0, verbose_name='\u6628\u865a\u5b9e\u5ea6')),
                ('CurrDelta', models.FloatField(default=0, verbose_name='\u4eca\u865a\u5b9e\u5ea6')),
                ('UpdateTime', models.CharField(default=b'', max_length=9, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('UpdateMillisec', models.IntegerField(default=0, verbose_name='\u6700\u540e\u4fee\u6539\u6beb\u79d2')),
                ('BidPrice1', models.FloatField(default=0, verbose_name='\u7533\u4e70\u4ef7\u4e00')),
                ('BidVolume1', models.IntegerField(default=0, verbose_name='\u7533\u4e70\u91cf\u4e00')),
                ('AskPrice1', models.FloatField(default=0, verbose_name='\u7533\u5356\u4ef7\u4e00')),
                ('AskVolume1', models.IntegerField(default=0, verbose_name='\u7533\u5356\u91cf\u4e00')),
                ('BidPrice2', models.FloatField(default=0, verbose_name='\u7533\u4e70\u4ef7\u4e8c')),
                ('BidVolume2', models.IntegerField(default=0, verbose_name='\u7533\u4e70\u91cf\u4e8c')),
                ('AskPrice2', models.FloatField(default=0, verbose_name='\u7533\u5356\u4ef7\u4e8c')),
                ('AskVolume2', models.IntegerField(default=0, verbose_name='\u7533\u5356\u91cf\u4e8c')),
                ('BidPrice3', models.FloatField(default=0, verbose_name='\u7533\u4e70\u4ef7\u4e09')),
                ('BidVolume3', models.IntegerField(default=0, verbose_name='\u7533\u4e70\u91cf\u4e09')),
                ('AskPrice3', models.FloatField(default=0, verbose_name='\u7533\u5356\u4ef7\u4e09')),
                ('AskVolume3', models.IntegerField(default=0, verbose_name='\u7533\u5356\u91cf\u4e09')),
                ('BidPrice4', models.FloatField(default=0, verbose_name='\u7533\u4e70\u4ef7\u56db')),
                ('BidVolume4', models.IntegerField(default=0, verbose_name='\u7533\u4e70\u91cf\u56db')),
                ('AskPrice4', models.FloatField(default=0, verbose_name='\u7533\u5356\u4ef7\u56db')),
                ('AskVolume4', models.IntegerField(default=0, verbose_name='\u7533\u5356\u91cf\u56db')),
                ('BidPrice5', models.FloatField(default=0, verbose_name='\u7533\u4e70\u4ef7\u4e94')),
                ('BidVolume5', models.IntegerField(default=0, verbose_name='\u7533\u4e70\u91cf\u4e94')),
                ('AskPrice5', models.FloatField(default=0, verbose_name='\u7533\u5356\u4ef7\u4e94')),
                ('AskVolume5', models.IntegerField(default=0, verbose_name='\u7533\u5356\u91cf\u4e94')),
                ('AveragePrice', models.FloatField(default=0, verbose_name='\u5f53\u65e5\u5747\u4ef7')),
                ('ActionDay', models.CharField(default=b'', max_length=9, verbose_name='\u4e1a\u52a1\u65e5\u671f')),
            ],
        ),
    ]
