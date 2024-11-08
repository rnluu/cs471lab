from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # عنوان الكتاب
    author = models.CharField(max_length=100)  # مؤلف الكتاب
    published_date = models.DateField()         # تاريخ النشر
    isbn = models.CharField(max_length=13)      # رقم ISBN

    def __str__(self):
        return self.title  # طريقة لتمثيل الكائن كـ سلسلة نصية
