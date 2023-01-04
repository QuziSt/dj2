from django.shortcuts import render


def get_recipes():
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }
    return DATA


def show_index_page(request):
    return render(request, 'index.html',)


def check_persons_amount(request):
    persons = request.GET.get('servings')
    recipe = get_recipes()
    if persons:
        for dish in recipe:
            for ingredient in recipe[dish]:
                recipe[dish][ingredient] *= int(persons)
    return recipe


def show_omlet_recipe(request):
    recipe = check_persons_amount(request)
    context = {
        'recipe': recipe['omlet']
    }
    return render(request, 'calculator/index.html', context)


def show_pasta_recipe(request):
    recipe = check_persons_amount(request)
    context = {
        'recipe': recipe['pasta']
    }
    return render(request, 'calculator/index.html', context)


def show_buter_recipe(request):
    recipe = check_persons_amount(request)
    context = {
        'recipe': recipe['buter']
    }
    return render(request, 'calculator/index.html', context)
