"""Practice with dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 5, "strawberry": 8}

ice_cream["mint"] = 3

ice_cream.pop("mint")

print(ice_cream)