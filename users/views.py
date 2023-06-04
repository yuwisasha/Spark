from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileCreationForm, ProfileImageForm
from django.forms import modelformset_factory
from .models import ProfileImage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('create_profile')
    else:
        form = UserRegistrationForm()
    return render(request=request,
                  template_name='users/register.html',
                  context={'form': form})


class CreateProfileView(APIView):
    permission_classes = (IsAuthenticated, )

    def create_profile(request):

        ImageFormSet = modelformset_factory(ProfileImage,
                                            form=ProfileImageForm, extra=6)

        if request.method == 'POST':

            profile_form = ProfileCreationForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=ProfileImage.objects.none())

            if profile_form.is_valid() and formset.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()

                for form in formset.cleaned_data:
                    if form:
                        image = form['image']
                        photo = ProfileImage(profile=profile_form, image=image)
                        photo.save()

                return render(request, '/')
        else:
            profile_form = ProfileCreationForm()
            formset = ImageFormSet(queryset=ProfileImage.objects.none())
        return render(request=request,
                      template_name='users/create_profile.html',
                      context={'profile_form': profile_form,
                               'formset': formset})
