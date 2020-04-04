from django.contrib import admin
from . models import Article,Comment # Bu klasörde ki models.py içinden Article sınıfını dahil ettik. 
# Register your models here.
# admin.site.register(Article)
# decarator
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title"] # Makalenin başlık bilgisi görüntülenir.
    class meta:
        model=Article
    search_fields=["title"] # Başlığa göre arama eklenir. 
    list_filter=["created_date"] # Sağ kısma bir zaman filtresi ekler.
