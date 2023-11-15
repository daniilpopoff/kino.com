from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PersonForm


# create person

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно добавлен</h1><a href="/person_list/">Перейти</a>')
    else:
        form = PersonForm()

    return render(request, template_name='create_person.html', context={'form': form})


# delete person
def delete_person(request, id):
    if request.method == 'GET':
        person_id = get_object_or_404(Post, id=id)
        person_id.delete()
        return HttpResponse('<h1>Успешно добавлен</h1><a href="/person_list/">Перейти</a>')


# update person
def update_person(request, id):
    person_id = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PersonForm(instance=person_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно Обновлен</h1><a href="/person_list/">Перейти</a>')
    else:
        form = PersonForm(instance=person_id)
        context = {
            'form': form,
            'person_id': person_id
        }
    return render(request, template_name='update_person.html', context=context)


def person_list(request):
    if request.method == 'GET':
        person = Post.objects.all()
        return render(request, template_name='person_list.html', context={'person': person})
