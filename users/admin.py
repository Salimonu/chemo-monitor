from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

# class MyUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         ('Custom fields', {'fields': ('role',)}),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Custom fields', {'fields': ('role',)}),
#     )

# admin.site.register(MyUser, MyUserAdmin)


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom fields', {'fields': ('role', 'verification_requested', 'is_verified_clinician')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom fields', {'fields': ('role', 'verification_requested', 'is_verified_clinician')}),
    )
