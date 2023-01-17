from django.contrib import admin
from .models import Post, steps, mat_and_content

class PostAdmin(admin.ModelAdmin):
    list_display = ('Primary_key','author','title','slug','status','created_on')
    list_filter = ("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}
    
class stepsAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'image', 'step_desc','exp_step')
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('Material', 'Quantity', 'Mat_and_cont_Key')
     
admin.site.register(Post, PostAdmin)
admin.site.register(steps, stepsAdmin)
admin.site.register(mat_and_content, MaterialAdmin)

# Register your models here.
