from django.shortcuts import render, get_object_or_404
from .models import Show

def tvShowList(request):
    show = Show.objects.all()
    return render(request, 'tvshow/show_list.html', {'show': show})


def tvShowDetail(request, id):
    show_id = get_object_or_404(Show, id=id)
    return render(request, 'tvshow/show_detail.html', {'show_id': show_id})