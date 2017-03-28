from django.contrib import admin
from joins.models import join,uploads
class joinAdmin(admin.ModelAdmin):
    


    list_display=['f_name','l_name','email','ref_id']
    class Meta:
        model=join
        
        
admin.site.register(join,joinAdmin)

admin.site.register(uploads)
