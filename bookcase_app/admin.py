from django.contrib import admin

from . import models


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'status', 'return_back_day')

    fieldsets = (
        ("Information of the book", {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'return_back_day')
        }),
    )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'birthday')
    fields = ['fname', 'lname', 'birthday']


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    # fields =
