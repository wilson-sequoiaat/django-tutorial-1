from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dict = {
    "january": "January page",
    "february": "February page",
    "march": "March page",
    "april": "April page",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse(monthly_challenges, args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = monthly_challenges_dict.keys()
    month = list(months)[month - 1]
    redirect_path = reverse("monthly-challenge", args=[month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("This month is not supported")
