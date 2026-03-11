

from rest_framework import serializers
from .models import InstitutionStats, Notice, News, Content, Teacher, Video, Event


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Content
        fields = '__all__'
        
        def get_image_url(self, obj):
            if obj.image_url:
                return obj.image_url.url
            return None

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
        
# serializers.py
class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionStats
        fields = '__all__'     
        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'             
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'                     