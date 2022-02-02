from django import forms
from trainee.models import Trainee,Track,Intake


class AddTraineeModelForm(forms.ModelForm):
    # track_name = forms.ModelChoiceField(choices=[(track.id, track.name) for track in Track.objects.all()], empty_label="Select Track", label='Track')
    # intake_name = forms.ModelChoiceField(queryset=Intake.objects.all(), empty_label="Select Intake", label='Intake')

    class Meta:
        model = Trainee
        fields = ["name"]
