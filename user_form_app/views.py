from django.shortcuts import render, redirect
from .forms import UserFormForm
from django.core.mail import send_mail
from django.conf import settings
from .models import UserForm


def user_form(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            form.save()

            # Send email to the form submitter
            subject = 'Form Submission Confirmation'
            message = 'Thank you for submitting the form!'
            from_email = settings.EMAIL_HOST_USER
            to_email = [form.cleaned_data['email']]
            send_mail(subject, message, from_email, to_email)

            return redirect('submitted_forms')
    else:
        form = UserFormForm()
    return render(request, 'user_form_app/user_form.html', {'form': form})
    return redirect('submitted_forms')


def submitted_forms(request):
    forms = UserForm.objects.all()
    return render(request, 'user_form_app/submitted_forms.html', {'forms': forms})
