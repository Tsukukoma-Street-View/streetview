from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic

from .models import Scene, RelatedScene, Event, LiveEvent

class HomeView(generic.TemplateView):
    template_name = 'streetview/home.html'


def scene_view(request):
    live_event_list = LiveEvent.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now()).order_by('end_date')[:10]
    next_live_event_list = LiveEvent.objects.filter(start_date__gt=timezone.now()).order_by('start_date')[:3]

    context = {
        'live_event_list': live_event_list,
        'next_live_event_list': next_live_event_list,
    }
    return render(request, 'streetview/view.html', context)


def ajax_transition(request):
    scene_id = request.GET.get('id')
    scene = Scene.objects.get(id=scene_id)
    scene_name = scene.name
    default_direction = scene.default_direction
    scene_image_url = scene.image.url

    relatedscene_list = RelatedScene.objects.all().filter(parent_scene=scene)
    relatedscene_id = [relatedscene.scene_id for relatedscene in relatedscene_list]
    relatedscene_r = [relatedscene.r for relatedscene in relatedscene_list]
    relatedscene_theta = [relatedscene.theta for relatedscene in relatedscene_list]
    relatedscene_button_size = [relatedscene.button_size for relatedscene in relatedscene_list]

    prev_scene_theta = request.GET.get('theta')

    event_list = Event.objects.all().filter(scene=scene)
    event_r = [event.r for event in event_list]
    event_theta = [event.theta for event in event_list]
    event_image_url = [event.image.url for event in event_list]
    event_name = [event.event_name for event in event_list]
    event_group_name = [event.group_name for event in event_list]
    event_hp_url = [event.hp_url for event in event_list]
    event_twitter_url = [event.twitter_url for event in event_list]
    event_youtube_url = [event.youtube_url for event in event_list]

    d = {
        'scene_id': scene_id,
        'scene_name': scene_name,
        'default_direction': default_direction,
        'scene_image_url': scene_image_url,
        'relatedscene_id': relatedscene_id,
        'relatedscene_r': relatedscene_r,
        'relatedscene_theta': relatedscene_theta,
        'relatedscene_button_size': relatedscene_button_size,
        'prev_scene_theta': prev_scene_theta,
        'event_r': event_r,
        'event_theta': event_theta,
        'event_image_url': event_image_url,
        'event_name': event_name,
        'event_group_name': event_group_name,
        'event_image_url': event_image_url,
        'event_hp_url': event_hp_url,
        'event_twitter_url': event_twitter_url,
        'event_youtube_url': event_youtube_url,
    }
    return JsonResponse(d)
