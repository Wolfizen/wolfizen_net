from django.forms import ModelForm, Form
from django.forms.models import ModelChoiceField

from wolfizen_net.apps.rsfa_voting.models import Show


class CreateShowForm(ModelForm):
    class Meta:
        model = Show
        fields = ['name']


class VoteForm(Form):
    show = ModelChoiceField(queryset=Show.objects.all())
