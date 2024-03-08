"""Creating my garden functions."""

__author__ = "730475919"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
print(by_kind)

new_plant: str = "elderberry"
new_plant_kind: str = "fruit"

class Garden_Functions:


    def add_by_kind(by_kind: dict[str, list[str]], plant_kind: str, plant_name: str) -> None:
        """Adds a plant to the garden dictionary sorted by plant kind through mutation."""
        if plant_kind in by_kind:
            by_kind[plant_kind].append(plant_name)
            by_kind[plant_kind].sort()
        else:
            by_kind[plant_kind] = [plant_name]


    def add_by_date(by_kind: dict[str, list[str]], month: str, plant_name: str) -> None:
        """Adds a plant to the garden dictionary sorted by seed sowing date through mutation."""
        if month in by_kind:
            by_kind[month].append(plant_name)
        else:
            by_kind[month] = [plant_name]
        by_kind[month].sort()


    def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], kind: str, date: str) -> str:
        """Searches through both dictionaries and returns a list of what plants of a certain kind to plant at a certain date."""
        if kind in by_kind and date in by_date:
            plants_to_plant = [plant for plant in by_kind[kind] if plant in by_date[date]]
            if plants_to_plant:
                return f"{kind}s to plant in {date}: {plants_to_plant}"
            else:
                return f"No {kind}s to plant in {date}."
        else:
            return f"No {kind}s or {date} in the garden."

if __name__ == '__main__':
    __main__()