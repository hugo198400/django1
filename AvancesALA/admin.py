from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('ala',)}),
    )



from .models import CustomUser,Area, Ala, Punto, RegAvance

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Area)
admin.site.register(Ala)
admin.site.register(Punto)
admin.site.register(RegAvance)




