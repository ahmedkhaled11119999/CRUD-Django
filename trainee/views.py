from django.shortcuts import reverse
from django.views.generic import CreateView
from trainee.models import Trainee


class CreateTrainee(CreateView):
    model = Trainee
    fields = "__all__"

    def get_success_url(self):
        return reverse('home')


