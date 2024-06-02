from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    "january": "Follow a carnovre diet",
    "february": "Join the Gym",
    "march": "Join swimming class",
    "april": "Join MMA class",
    "may": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = monthly_challenges_dict.keys()
    month = list(months)[month - 1]
    redirect_path = reverse("monthly-challenge", args=[month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]

        # These two lines can be replaced by the render() method
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        return render(request, "challenges/challenge.html", {
            "challenge": challenge_text,
            "month": month
        })
    except:
        # These two lines can be replaced by the Http404 class
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        raise Http404()  # this will check for a 404.html file in the root "templates" folder
