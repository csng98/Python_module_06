def validate_ingredients(ingredients: list[str]) -> str:
	for i in ingredients:
		if i.lower() == ingredients:
			return ("VALID")
		else:
			return ("INVALID")
