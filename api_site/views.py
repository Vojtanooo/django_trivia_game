from django.shortcuts import redirect, render
from .get_api import get_question


def home(request):
    context = {
        "context": get_question(0)[0],
        "username": request.session.get("username"),
        "score": request.session.get("score")
    }

    if request.session["num"] == 9:
        request.session.clear()
        return redirect("success")  # doplnit stranku se skore a časem

    if request.method == "POST":
        num = request.session.get("num") + 1
        request.session["num"] = num

        if request.POST.get("button") in get_question(0)[1]:
            score = request.session.get("score") + 1
            request.session["score"] = score
            context.update({"context": get_question(num)[0], "score": score})
        else:
            context.update({"context": get_question(num)[0]})

    return render(request, "home.html", context)


def success(request):
    context = {}
    if "submit" in request.POST:
        request.session["username"] = request.POST.get("username")
        request.session["score"] = 0
        request.session["num"] = 0
        return redirect("home")
    return render(request, "success.html", context)
