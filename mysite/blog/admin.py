from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # Список отображаемых полей
    list_filter = ['status', 'created', 'publish', 'author']        # Фильтры по полям
    search_fields = ['title', 'body']                               # Поля по которым осуществляется текстовый поиск
    prepopulated_fields = {'slug': ('title',)}                      # Формирование слага из указанных полей
    raw_id_fields = ['author']                                      # Более удобное меню выбора плльзователя
    date_hierarchy = 'publish'                                      # Навигация по иерархии дат
    ordering = ['status', 'publish']                                # Порядок сортировки при отображении постов

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']