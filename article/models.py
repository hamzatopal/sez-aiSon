from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):  # Model nesnesinden türetiyoruz. 
    author=models.ForeignKey("auth.User", verbose_name=(""), on_delete=models.CASCADE)  
    # auth.User aslında django admin içinde var ikincil anahtar ile o tablo modeline bağlanılıyoruz.
    # models.CASCADE model silinirse onunla alakalı ne varsa silinsin demektir.
    title= models.CharField(max_length=50)
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True) # Eklenme zamanı otamatikleştirmek için.
    article_image=models.FileField(blank=True,null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_date']    
class Comment(models.Model):
    article=models.ForeignKey(Article, verbose_name="Makale", on_delete=models.CASCADE,related_name='comments')
    comment_author=models.CharField(max_length=50,verbose_name='isim')
    comment_content=models.CharField(max_length=500,verbose_name='yorum')
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=['-comment_date']


