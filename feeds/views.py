from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FeedSerializer
from rest_framework.generics import ListAPIView

from feeds.models import Feed


class FeedsView(generic.ListView):
    model = Feed
    fields = ["text", "author"]
    template_name = "feeds/feeds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["feeds"] = super().get_queryset()

        return context

class FeedsAPIView(ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedView(generic.DetailView):
    model = Feed
    template_name = "feeds/feed.html"


class FeedCreateView(generic.CreateView):
    model = Feed
    fields = ["text"]
    template_name = "feeds/create.html"

    def get_success_url(self):
        return reverse_lazy("feeds")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        error_message = "Enthält verbotene Wörter"
        messages.error(self.request, error_message)
        return response


class FeedUpdateView(generic.UpdateView):
    model = Feed
    fields = ["text"]
    template_name = "feeds/update.html"

    def get_success_url(self):
        return reverse_lazy("feed", args=[self.object.pk])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update"] = True
        return context

def feed_delete(request, pk):
    feed = Feed.objects.get(pk=pk)

    if request.method == "POST":
        feed.delete()
        return redirect("feeds")

    return (request, "feeds/delete.html", {"feed": feed})
