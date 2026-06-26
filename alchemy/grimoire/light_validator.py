def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients = [item.lower() for item in light_spell_allowed_ingredients()]
    ingredients_list = [item.strip().lower() for item in ingredients.split(",") if item.strip()]

    if any(ingredient in allowed_ingredients for ingredient in ingredients_list):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
