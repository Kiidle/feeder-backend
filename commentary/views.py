from django.views import generic

from commentary.models import Commentary

class CommentaryView(generic.DetailView):
    model = Commentary
    template_name = "commentary/commentary.html"