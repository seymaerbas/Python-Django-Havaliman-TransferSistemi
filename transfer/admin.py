from django.contrib import admin

# Register your models here.
from transfer.models import Category, Transfer, Images

class TransferImageInline(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class TransferAdmin(admin.ModelAdmin):

    list_display = ['title', 'category', 'base_price', 'km_price', 'capasity', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [TransferImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'transfer', 'image_tag']
    readonly_fields = ('image_tag',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Images, ImagesAdmin)
