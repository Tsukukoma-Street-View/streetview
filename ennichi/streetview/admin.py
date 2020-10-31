from django.conf import settings
from django.contrib import admin

from .models import Scene, RelatedScene, Event, LiveEvent


admin.site.site_header = 'サイト管理'
admin.site.index_title = '筑駒縁日班'


class RelatedSceneInline(admin.StackedInline):
    model = RelatedScene
    fields = ('scene_id', 'direction', 'r', 'theta', 'button_size')
    extra = 1


class SceneAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'id', 'name', 'default_direction',  'image',
            ),
        }),
    )
    inlines = [RelatedSceneInline,]
    list_display = ('id', 'name',)
    
admin.site.register(Scene, SceneAdmin)


class LiveEventInline(admin.StackedInline):
    model = LiveEvent
    fields = 'name', 'start_date', 'end_date', 'image', 'live_url'
    extra = 1


class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'scene', 'hp_url', 'twitter_url', 'youtube_url', 'group_name', 'event_name',
                'image', 'description', 'r', 'theta',
            ),
        }),
    )
    inlines = [LiveEventInline,]
    list_display = ('group_name', 'event_name', 'scene')

admin.site.register(Event, EventAdmin)
