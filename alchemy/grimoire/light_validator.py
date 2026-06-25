def validate_ingredients(ingredients: str, allowed_ingredients: list[str]) -> str:
    ingredients_list = [item.strip().lower() for item in ingredients.split(",")]

    for ingredient in ingredients_list:
        if ingredient not in allowed_ingredients:
            return "INVALID"
    return "VALID"
