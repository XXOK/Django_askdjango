from django.views.generic import View, TemplateView
from django.shortcuts import HttpResponse


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_string_name().format(name=name)
        return HttpResponse(html)

    def get_string_name(self):
        return '''
            {name}
            <p>옴바니 반메홈</p>
        '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()