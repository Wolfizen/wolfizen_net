import hashlib

from django.conf import settings
from django.forms import Form, CharField, Textarea
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from wolfizen_net.apps.deeplistening.project import generate_composition as generate_composition_module
from wolfizen_net.apps.deeplistening.project.generate_composition import load_all_sound_clips, generate_composition

import os.path


class GenerativeCompositionView(View):

    def get(self, request: HttpRequest):
        # Show a blank input form
        return render(
            request,
            "deeplistening/generative_composition_input.html",
            context={'form': GenerativeCompositionForm()})

    def post(self, request: HttpRequest):
        form = GenerativeCompositionForm(request.POST)
        if not form.is_valid():
            # Show the input form, with errors stored in the Form object
            return render(request, "deeplistening/generative_composition_input.html", context={'form': form})
        else:
            # Run the composition generation program
            seed_text = form.cleaned_data['seed_text']
            sound_library = load_all_sound_clips(
                os.path.join(os.path.dirname(os.path.abspath(generate_composition_module.__file__)), "sound_library"))
            composition = generate_composition(sound_library, seed_text)
            filename = "generative_composition_" + hashlib.md5(seed_text.encode("utf-8")).hexdigest() + ".mp3"
            composition.export(os.path.join(settings.MEDIA_ROOT, filename), format="mp3")
            return render(
                request,
                "deeplistening/generative_composition_output.html",
                context={'audio_url': settings.MEDIA_URL + filename, 'seed_text': seed_text})


class GenerativeCompositionForm(Form):
    seed_text = CharField(label="Input seed", max_length=1000, widget=Textarea)


