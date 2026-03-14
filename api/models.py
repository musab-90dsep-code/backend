from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import Field


class Notice(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    image_url = CloudinaryField('image', blank=True, null=True)
    content = models.TextField(verbose_name="Detailed News", blank=True, null=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=255)
    image_url = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title
    
import re

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True)
    video_url = models.URLField(help_text="YouTube or Video Link")

    def get_thumbnail_url(self):
        # ইউটিউব ভিডিও আইডি এক্সট্র্যাক্ট করার জন্য রেগুলার এক্সপ্রেশন
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', self.video_url)
        if video_id_match:
            video_id = video_id_match.group(1)
            # ইউটিউবের হাই কোয়ালিটি থাম্বনেইল ইউআরএল
            return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        return None # অন্য কোনো প্ল্যাটফর্ম হলে বা আইডি না পেলে

    def __str__(self):
        return self.title
    
class InstitutionStats(models.Model):
    # আইকন চেনার জন্য একটি ছোট নাম (যেমন: students, teachers, results)
    slug = models.SlugField(unique=True, help_text="Identifier for the stat (e.g., students, teachers)")
    
    # সংখ্যাটি দেখানোর জন্য (যেমন: ৫০০+)
    number = models.CharField(max_length=50, help_text="Example: 500+, 100%, 50+")
    
    # নিচের ছোট লেখাটি (যেমন: Total Students)
    label_en = models.CharField(max_length=100, help_text="Label in English")
    label_bn = models.CharField(max_length=100, help_text="Label in Bengali")
    
    # সর্টিং করার জন্য (১, ২, ৩, ৪ এভাবে সাজাতে)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Institution Stat"
        verbose_name_plural = "Institution Stats"

    def __str__(self):
        return f"{self.label_bn} - {self.number}"
    
class Teacher(models.Model):
    # Teacher er chobi
    image_url = CloudinaryField('image', blank=True, null=True)
    
    # Name field (Dui bhashay)
    name_en = models.CharField(max_length=255, verbose_name="Name (English)")
    name_bn = models.CharField(max_length=255, verbose_name="Name (Bangla)")
    
    # Designation/Role field (Dui bhashay)
    role_en = models.CharField(max_length=255, verbose_name="Role (English)")
    role_bn = models.CharField(max_length=255, verbose_name="Role (Bangla)")
    
    # Biography field (Dui bhashay)
    bio_en = models.TextField(verbose_name="Bio (English)")
    bio_bn = models.TextField(verbose_name="Bio (Bangla)")
    
    # Priority (Jate kake age dekhabe seta thhik kora jay)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name_en
    
    


class Event(models.Model):
    # ইভেন্টের ছবি
    image_url = CloudinaryField('image', blank=True, null=True)
    
    # শিরোনাম (বাংলা ও ইংরেজি)
    title_en = models.CharField(max_length=255, verbose_name="Title (English)")
    title_bn = models.CharField(max_length=255, verbose_name="Title (Bangla)")
    
    # তারিখ, সময় এবং স্থান
    date_en = models.CharField(max_length=100, verbose_name="Date (English)")
    date_bn = models.CharField(max_length=100, verbose_name="Date (Bangla)")
    
    time_en = models.CharField(max_length=100, verbose_name="Time (English)")
    time_bn = models.CharField(max_length=100, verbose_name="Time (Bangla)")
    
    location_en = models.CharField(max_length=255, verbose_name="Location (English)")
    location_bn = models.CharField(max_length=255, verbose_name="Location (Bangla)")
    
    # বর্ণনা (বাংলা ও ইংরেজি)
    desc_en = models.TextField(verbose_name="Description (English)")
    desc_bn = models.TextField(verbose_name="Description (Bangla)")
    
    # ইভেন্টের ক্রম নির্ধারণের জন্য
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en