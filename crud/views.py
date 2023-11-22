from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from .forms import PersonForm
from django.views import generic



#ListView
class PersonListView(generic.ListView):
    template_name = 'crud/person_list.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return self.queryset

#Detail View
class PersonDetailView(generic.DetailView):
    template_name = 'crud/person_detail.html'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=person_id)


# create person

class CreatePersonView(generic.CreateView):
    template_name = 'crud/create_person.html'
    queryset = models.Post.objects.all()
    form_class = PersonForm
    success_url = "/person_list/"


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePersonView, self).form_valid(form=form)



# def create_person(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Успешно добавлен</h1><a href="/person_list/">Перейти</a>')
#     else:
#         form = PersonForm()
#
#     return render(request, template_name='create_person.html', context={'form': form})


class DeletePersonView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/person_list/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=person_id)

# delete person
# def delete_person(request, id):
#     if request.method == 'GET':
#         person_id = get_object_or_404(Post, id=id)
#         person_id.delete()
#         return HttpResponse('<h1>Успешно добавлен</h1><a href="/person_list/">Перейти</a>')
#

# update person
class UpdatePersonView(generic.UpdateView):
    template_name = 'crud/update_person.html'
    form_class = PersonForm
    success_url = '/person_list/'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=person_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdatePersonView, self).form_valid(form=form)



# def update_person(request, id):
#     person_id = get_object_or_404(Post, id=id)
#     if request.method == 'POST':
#         form = PersonForm(instance=person_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Успешно Обновлен</h1><a href="/person_list/">Перейти</a>')
#     else:
#         form = PersonForm(instance=person_id)
#         context = {
#             'form': form,
#             'person_id': person_id
#         }
#     return render(request, template_name='update_person.html', context=context)

#
# def person_list(request):
#     if request.method == 'GET':
#         person = Post.objects.all()
#         return render(request, template_name='person_list.html', context={'person': person})



