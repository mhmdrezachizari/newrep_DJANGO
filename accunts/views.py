from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm
from .models import OtpCode
from extensions.otp import send_otp
import random
# Create your views here.
class USERREGISTER(View):
    forms_class = UserRegistrationForm
    template_name = 'accunts\eegister.html'
    def get(self, request):
        form = self.forms_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.forms_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone_number = cd['phone_number']
            code = random.randint(1000, 9999)
            send_otp(code , phone_number)
            OtpCode.objects.create(code=code , phone_number=phone_number )
            request.session['user'] = {
                "phone_number": phone_number,
                "email": cd["email"],
                "about_me": cd["about_me"],
                "first_name": cd["first_name"],
                "last_name": cd["last_name"],
                "password": cd["password2"],
            }
            return redirect("accounts:verify")
        return render(request, self.template_name, {"form": form})



