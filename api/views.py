

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InstitutionStats, Notice, News, Content, Teacher, Video, Event
from .serializers import EventSerializer, NoticeSerializer, NewsSerializer, ContentSerializer, StatsSerializer, TeacherSerializer, VideoSerializer

@api_view(['GET'])
def get_all_content(request):

    notices = Notice.objects.all().order_by('-id')
    news = News.objects.all().order_by('-id')
    contents = Content.objects.all()
    videos = Video.objects.all()
    stats = InstitutionStats.objects.all().order_by('order')[:4]
    teachers = Teacher.objects.all().order_by('order')
    events = Event.objects.all().order_by('order', '-id')[:4]

    return Response({
        "notices": NoticeSerializer(notices, many=True).data,
        "news": NewsSerializer(news, many=True, context={'request': request}).data, # context যোগ করা হয়েছে
        "contents": ContentSerializer(contents, many=True, context={'request': request}).data, # context যোগ করা হয়েছে
        "videos": VideoSerializer(videos, many=True, context={'request': request}).data,
        "stats": StatsSerializer(stats, many=True).data,
        "teachers": TeacherSerializer(teachers, many=True, context={'request': request}).data,
        "events": EventSerializer(events, many=True, context={'request': request}).data,
    })