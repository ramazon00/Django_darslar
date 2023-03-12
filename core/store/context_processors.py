from .models import Category

def my_category(request):

    menu_categories = Category.objects.all()


    return {"my_category":menu_categories}