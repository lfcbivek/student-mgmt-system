from django.contrib import admin
from .models import Waitlist
# Register your models here.
class WaitListAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'notes','created_at','updated_at')
    search_fields = ('first_name',)


admin.site.register(Waitlist,WaitListAdmin)