from light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
	allowed = ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
	if validate_ingredients(ingredients) == "VALID":
		return (f"Spell recorded: {spell_name} - VALID")
	else:
		return ("Spell rejected")
