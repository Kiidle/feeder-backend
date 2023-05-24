from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from commentary.models import Commentary
from feeds.models import Feed
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CommentarySerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class CommentariesAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer

class CommentaryView(generic.DetailView):
    model = Commentary
    template_name = "commentary/commentary.html"


class CommentaryAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ["text"]
    template_name = "commentary/create.html"

    def get_success_url(self):
        return reverse_lazy("feed", kwargs={"pk": self.kwargs.get("feed_id")})

    def get_current_feed(self, **kwargs):
        return Feed.objects.get(id=self.kwargs.get("feed_id"))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        feed = self.get_current_feed(**kwargs)
        data.update({"feed": feed})
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.feed = self.get_current_feed(**self.kwargs)
        return super().form_valid(form)


class CommentaryCreateAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentarySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['feed_id'] = self.kwargs['feed_id']  # Update this line
        return context

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, feed_id=self.kwargs['feed_id'])

class CommentaryUpdateView(generic.UpdateView):
    model = Commentary
    fields = ["text"]
    template_name = "commentary/update.html"

    def get_success_url(self):
        return reverse_lazy("commentary", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentaryUpdateAPIView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feed.objects.all()
    serializer_class = CommentarySerializer


def commentary_delete(request, pk):
    commentary = Commentary.objects.get(pk=pk)

    if request.method == "POST":
        feed_id = commentary.feed.id
        commentary.delete()
        return redirect("feed", pk=feed_id)

    return (request, "commentary/delete.html", {"commentary": commentary})


class CommentaryDeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feed.objects.all()
    serializer_class = CommentarySerializer
