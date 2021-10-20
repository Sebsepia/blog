from django.contrib import admin
from .models import Post, BlogImage, PanoImage, PortfolioCategory, SketchbookCategory


class BImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0

class PImageInline(admin.TabularInline):
    model = PanoImage
    extra = 0

class PostInline(admin.TabularInline):
    model = Post

    exclude = ('title_tag','slug','talkshit','talkshit_md','tags')
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'tags' )
    fields = [('title', 'title_tag', 'slug'),('talkshit'),('tags','post_date'),('portfolio_category', 'sketchbook_category')]
    inlines = [ BImageInline, PImageInline]
admin.site.register(Post, PostAdmin)

class PortfolioCatAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fields = [('category_name', )]
    inlines = [PostInline]
admin.site.register(PortfolioCategory, PortfolioCatAdmin)

class SketchbookCatAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    fields = [('category_name', )]
    inlines = [PostInline]
admin.site.register(SketchbookCategory, SketchbookCatAdmin)
