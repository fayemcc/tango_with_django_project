import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page


def populate():

    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask", "url": "http://flask.pocoo.org"}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64}, "Django": {"pages": django_pages, "views": 64, "likes": 32}, "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    for cat, cat_dict in cats.items():
        c = add_cat(cat, cat_dict["views"], cat_dict["likes"])
        i = 10
        for p in cat_dict["pages"]:
            add_page(c, p["title"], p["url"], i)
            i += 10

    for c in Category.objects.all():
        print("<Category: {0}, {1} views, {2} likes".format(str(c), c.views, c.likes))
        for p in Page.objects.filter(category=c):
            print("- {0}- {1}".format(str(c), str(p)))


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    if not views == 0:
        c.views = views
    if not likes == 0:
        c.likes = likes
    c.save()
    return c


def add_page(cat, title, url, views):
    P = Page.objects.get_or_create(category=cat, title=title)[0]
    P.url = url
    P.views = views
    P.save()
    return P


if __name__ == '__main__':
    print("Starting rango population script...")
    populate()
