from django.contrib import admin

# Register your models here.

from .models import Product,Profile,Course



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')  # Add search capability
    list_filter = ('price',) 

admin.site.register(Product,ProductAdmin)   

admin.site.register(Profile)   

admin.site.register(Course)



# # admin.py
# from django.contrib import admin
from .models import Author, Book

# Register Author model
                 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display author names in the list view
admin.site.register(Author,AuthorAdmin)


# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # Display title, author, and publication date
    list_filter = ('author',)  # Add filter by author in the list view
    search_fields = ('title', 'author__name')  # Allow searc