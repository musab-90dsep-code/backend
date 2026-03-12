from rest_framework import serializers
from .models import InstitutionStats, Notice, News, Content, Teacher, Video, Event

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    # image_url কে ফুল লিঙ্কে রূপান্তর করার জন্য SerializerMethodField ব্যবহার


    class Meta:
        model = News
        fields = '__all__'



class ContentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = '__all__'
    
    # এই ফাংশনটি Meta ক্লাসের বাইরে থাকবে (ইন্ডেন্টেশন খেয়াল করুন)
    def get_image_url(self, obj):
        if obj.image_url:
            return obj.image_url.url
        return None

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

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

