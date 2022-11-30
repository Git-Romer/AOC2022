from django.contrib import admin
from scoreboard.models import jsoncrawler

# Register your models here.
class AdminSettings(admin.ModelAdmin):
    list_display = ['name', 'member_id', 'stars']

admin.site.register(jsoncrawler, AdminSettings)