from rest_framework import serializers
from .models import InstitutionStats, Notice, News, Content, Teacher, Video, Event

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            if obj.image_url:
                return obj.image_url.url
        except Exception:
            # যদি ইমেজে কোনো সমস্যা থাকে, তাহলে সার্ভার ক্র্যাশ না করে None রিটার্ন করবে
            return None
        return None

class ContentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = '__all__'
    
    def get_image_url(self, obj):
        try:
            if obj.image_url:
                return obj.image_url.url
        except Exception:
            return None
        return None

class TeacherSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = '__all__' 
       
    def get_image_url(self, obj):
        try:
            if obj.image_url:
                return obj.image_url.url
        except Exception:
            return None
        return None

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            if obj.image_url:
                return obj.image_url.url
        except Exception:
            return None
        return None

class VideoSerializer(serializers.ModelSerializer):
    # এই লাইনটি যোগ করতে হবে
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    # এই ফাংশনটি Cloudinary থেকে সম্পূর্ণ লিংক বের করে আনবে
    def get_video_url(self, obj):
        try:
            if obj.video_url:
                if hasattr(obj.video_url, 'url'):
                    return obj.video_url.url
                return str(obj.video_url)
        except Exception:
            return None
        return None

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionStats
        fields = '__all__'