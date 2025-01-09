spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []

    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    
    return spiciest_foods

get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')


def get_average_heat_level(spicy_foods):
    heat_level_start = 0

    for food in spicy_foods:
        heat_level_start += food["heat_level"]
    
    return(heat_level_start / len(spicy_foods))

get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    new_list = []

    for food in spicy_foods:
        new_list.append(food)
    
    new_list.append(spicy_food)

    return new_list

create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
)
