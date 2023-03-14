from django.views import generic
from django.shortcuts import redirect
from feeds.models import Feed
<<<<<<< Updated upstream
from commentary.models import Commentary
from authentication.models import User
=======
from django.urls import reverse_lazy
>>>>>>> Stashed changes


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
