from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import redirect
from feeds.models import Feed
from commentary.models import Commentary
from authentication.models import User
from django.urls import reverse_lazy


class FeedsView(generic.ListView):

    model = Feed
    fields = ["text", "author"]
    template_name = "feeds/feeds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["feeds"] = super().get_queryset()

        print(context)

        return context

class FeedView(generic.DetailView):
    model = Feed
    template_name = "feeds/feed.html"

def feed_create():
    return
def feed_edit():
    return
def feed_delete():
    return

class FeedCreateView(generic.CreateView):
    model = Feed
    fields = ['text']
    template_name = "feeds/create.html"

    def get_success_url(self):
        return reverse_lazy('feeds')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def feed_delete(request, pk):
    feed = Feed.objects.get(pk=pk)

    if request.method == 'POST':
        feed.delete()
        return redirect('feeds')

    return (request, 'feeds/delete.html', {'feed': feed})