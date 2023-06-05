from random import sample

from django.views.generic import TemplateView

from app_blog.models import Post
from app_client.models import Client
from app_newsletter.models import Newsletter


class IndexPageView(TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_newsletters'] = Newsletter.objects.count()
        context['active_newsletters'] = Newsletter.objects.filter(is_active=True).count()
        context['unique_clients'] = Client.objects.values('email').distinct().count()

        all_posts = list(Post.objects.all())
        context['random_blog_posts'] = sample(all_posts, min(3, len(all_posts)))

        return context
