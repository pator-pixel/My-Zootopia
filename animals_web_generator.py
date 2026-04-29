import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    output += f"Name: {animal['name']}\n"

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f"Diet: {characteristics['diet']}\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"Location: {animal['locations'][0]}\n"

    if "type" in characteristics:
        output += f"Type: {characteristics['type']}\n"

    output += "\n"


with open("animals_template.html", "r", encoding="utf-8") as handle:
    html_template = handle.read()


new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(new_html)