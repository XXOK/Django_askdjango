from django.contrib import admin
from .models import Post,Comment,Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag_list', 'content_size', 'photo', 'status', 'created_at', 'updated_at']

    actions = ['make_draft', 'make_published', 'make_withdrawn']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(request, post):
        return ', '.join(tag.name for tag in post.tag_set.all())

    def content_size(self, Post):
        return '{}글자'.format(len(Post.content))
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        update_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경합니다.'.format(update_count))
    make_draft.short_description = '지정 포스팅을 draft 상태로 변경합니다.'

    def make_published(self, request, queryset):
        update_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경합니다.'.format(update_count))
    make_published.short_description = '지정 포스팅을 Published 상태로 변경합니다.'

    def make_withdrawn(self, request, queryset):
        update_count = queryset.update(status='w')
        self.message_user(request, '{}건의 포스팅을 withdrawn 상태로 변경합니다.'.format(update_count))
    make_withdrawn.short_description = '지정 포스팅을 withdrawn 상태로 변경합니다.'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'id', 'author', 'post_content_len', 'message', 'created_at', 'updated_at']
    # list_select_related = ['post']

    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        return qs.select_related('post')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass