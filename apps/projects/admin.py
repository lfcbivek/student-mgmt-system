from django.contrib import admin
from .models import Projects
# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','title','level')
    search_fields = ('id','level')
    
    
    
admin.site.register(Projects,ProjectsAdmin)