from light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
	allowed = ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
	allowed = light_spell_allowed_ingredients()
	result = validate_ingredients(ingredients, allowed)
	if result == "VALID":
		return (f"Spell recorded: {spell_name} "
            	f"({ingredients} - {result})")
	return "Spell rejected"
