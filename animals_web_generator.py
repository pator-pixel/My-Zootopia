import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Converts a single animal object into HTML"""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def main():
    animals_data = load_data("animals_data.json")

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)


if __name__ == "__main__":
    main()