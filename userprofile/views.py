from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from userprofile.models import User


class UserView(View):

    def get(self, request):
        users = User.objects.all()
        return render(
            request,
            'sod/profile.html',
            {'user_list': users}
        )
