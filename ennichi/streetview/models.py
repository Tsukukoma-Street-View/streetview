from datetime import datetime
from django.db import models
from django.utils import timezone

import math


class Scene(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    name = models.CharField('地名', max_length=30, default='', blank=True)
    image = models.ImageField('画像', upload_to='images/')
    default_direction = models.FloatField('画像の初期方向', default=0.0)  #視点を回転（前方0度時計回り）

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'シーン'
        verbose_name_plural = 'シーン'


class RelatedScene(models.Model):
    parent_scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    scene_id = models.IntegerField('シーンのID', default=0)
    direction = models.FloatField('画像の初期方向', default=0.0) #視点を回転（前方0度時計回り）
    r = models.FloatField(default=18.0)
    theta = models.FloatField(default=0.0) #ボタンを移動（前方0度時計回り）
    button_size = models.FloatField('ボタンのサイズ', default=5.0)


class Event(models.Model):
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, blank=True)
    hp_url = models.URLField('HPのURL', max_length=200, blank=True,)
    twitter_url = models.URLField('TwitterのURL', max_length=200, blank=True,)
    youtube_url = models.URLField('YoutubeのURL', max_length=200, blank=True,)
    group_name = models.CharField('団体名', max_length=50,)
    event_name = models.CharField('イベント名', max_length=50,)
    image = models.ImageField('画像', upload_to='images/')
    description = models.CharField('説明', max_length=1000, blank=True)
    r = models.FloatField(default=17.0)
    theta = models.FloatField(default=0.0)  #ボタンを移動（前方0度時計回り）

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'イベント'
        verbose_name_plural = 'イベント'


class LiveEvent(models.Model):
    parent_event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    name = models.CharField('ライブイベント名', max_length=50, default='')
    start_date = models.DateTimeField('開始日時', default=timezone.now)
    end_date = models.DateTimeField('終了日時', default=timezone.now)
    image = models.ImageField('画像', upload_to='images/')
    live_url = models.URLField('LiveのURL', max_length=200, blank=True,)