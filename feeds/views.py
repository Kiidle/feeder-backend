from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from feeds.serializers import FeedSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status

from feeds.models import Feed


class FeedsView(generic.ListView):
    model = Feed
    fields = ["text", "author"]
    template_name = "feeds/feeds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["feeds"] = super().get_queryset()

        return context

class FeedsViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generic.DetailView):
    model = Feed
    template_name = "feeds/feed.html"

class FeedViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

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

class FeedCreateAPIView(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeedSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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