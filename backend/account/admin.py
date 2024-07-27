from django.contrib import admin
from .models import User, FriendshipRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name',  'email', 'is_active']
    list_filter = [ 'first_name', 'last_name','slug', 'is_active']
    prepopulated_fields = {'slug':('username',)}
    date_hierarchy ='date_joined'
    search_fields = ('username', 'first_name', 'last_name', 'email')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []  # Для администратора все поля будут редактируемыми
        else:
            return ('username', 'first_name', 'last_name', 'slug', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined',)  # Для персонала только указанные поля будут только для чтения

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser



@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('created_for', 'created_by', 'status_display', 'created_at')
    list_filter = ('status',)
    search_fields = ('created_for__username', 'created_by__username')
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []  # Для администратора все поля будут редактируемыми
        else:
            return ('created_for', 'created_by', 'created_at', 'status')  # Для персонала только указанные поля будут только для чтения

    def status_display(self, obj):
        return dict(FriendshipRequest.STATUS_CHOICES)[obj.status]

    status_display.short_description = 'Статус'

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
