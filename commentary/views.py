from django.shortcuts import redirect
from django.views import generic

import commentary
from commentary.models import Commentary

class CommentaryView(generic.DetailView):
    model = Commentary
    template_name = "commentary/commentary.html"

def commentary_create(request):
    return

def commentary_edit(request, pk):
    return

def commentary_delete(request, pk):
    commentary = Commentary.objects.get(pk=pk)

    if request.method == 'POST':
        feed_id = commentary.feed.id
        commentary.delete()
        return redirect('feed', pk=feed_id)

    return (request, 'commentary/delete.html', {'commentary': commentary})