from django.contrib import admin
from .models import Product
# Register your models here.
 



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def get_form(self,request,obj=None, **kwargs):
        form = super().get_form(request, object, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['name'].disabled = True
        return form
    
    