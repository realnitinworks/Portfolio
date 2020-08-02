import os

from django.contrib.postgres import search as psql_search
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from blog.models import Post

from .forms import ContactForm
from .models import CertificateGroup, Project


def home(request):
    return render(request, "portfolio/home.html", {"active": "home"})


def feed(request):
    return render(request, "portfolio/feeds.html", {"active": "feeds"})


def search(request):
    query = request.GET.get("q")
    page_number = request.GET.get("page")

    search_vector = (
        psql_search.SearchVector("title", weight="A")
        + psql_search.SearchVector("body", weight="A")
        + psql_search.SearchVector("summary", weight="B")
    )
    search_query = psql_search.SearchQuery(query)
    posts = (
        Post.published.annotate(
            rank=psql_search.SearchRank(search_vector, search_query)
        )
        .filter(rank__gte=0.3)
        .order_by("-rank")
    )

    paginator = Paginator(posts, os.environ.get("SEARCH_RESULTS_PER_PAGE", 6))

    try:
        posts = paginator.page(number=page_number)
    except PageNotAnInteger:
        posts = paginator.page(number=1)  # first page
    except EmptyPage:
        posts = paginator.page(number=paginator.num_pages)  # last page

    return render(
        request,
        "portfolio/search.html",
        {"posts": posts, "active": "home", "query": query},
    )


def contact(request):
    sent = False

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            question = form.cleaned_data["question"]

            # send email
            subject = f"{name}({email}) has a question for you."
            message = question
            sender = os.environ.get("EMAIL_SENDER_EMAIL")
            send_mail(
                subject, message, from_email=sender, recipient_list=[sender],
            )
            sent = True
    else:
        form = ContactForm()

    return render(
        request,
        "portfolio/contact.html",
        {"active": "contact", "sent": sent, "form": form},
    )


def portfolio(request):
    projects = Project.objects.all()
    certificate_groups = CertificateGroup.objects.all()

    return render(
        request,
        "portfolio/portfolio.html",
        {"projects": projects, "certificate_groups": certificate_groups},
    )


def project_detail(request, id, slug):
    project = get_object_or_404(Project, id=id, slug=slug)

    return render(
        request, "portfolio/project/project_detail.html", {"project": project}
    )


def certificate_group_detail(request, id, slug):
    certificate_group = get_object_or_404(CertificateGroup, id=id, slug=slug)

    return render(
        request,
        "portfolio/certificate/certificate_group_detail.html",
        {"certificate_group": certificate_group},
    )
