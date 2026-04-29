import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    output += '<li class="cards__item">\n'

    # Titel
    output += f'  <div class="card__title">{animal["name"]}</div>\n'

    # Textblock
    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'


with open("animals_template.html", "r", encoding="utf-8") as handle:
    html_template = handle.read()


new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(new_html)