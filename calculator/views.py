from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    recipe_keys = list(DATA['omlet'].keys())
    recipe_values = list(DATA['omlet'].values())
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': {
        recipe_keys[0] : int(recipe_values[0]) * servings,
        recipe_keys[1] : float(recipe_values[1]) * servings,
        recipe_keys[2] : float(recipe_values[2]) * servings
      }
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    recipe_keys = list(DATA['pasta'].keys())
    recipe_values = list(DATA['pasta'].values())
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe' : {
            recipe_keys[0]: float(recipe_values[0]) * servings,
            recipe_keys[1]: float(recipe_values[1]) * servings
        }
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    recipe_keys = list(DATA['buter'].keys())
    recipe_values = list(DATA['buter'].values())
    servings = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            recipe_keys[0]: int(recipe_values[0]) * servings,
            recipe_keys[1]: int(recipe_values[1]) * servings,
            recipe_keys[2]: int(recipe_values[2]) * servings,
            recipe_keys[3]: int(recipe_values[3]) * servings
        }
    }
    return render(request, 'calculator/index.html', context)