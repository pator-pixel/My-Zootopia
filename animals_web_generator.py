import json


DATA_FILE = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Converts a single animal object into HTML"""
    output = ['<li class="cards__item">\n']

    if "name" in animal:
        output.append(f'  <div class="card__title">{animal["name"]}</div>\n')

    output.append('  <p class="card__text">\n')

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output.append(f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n')

    if "locations" in animal and len(animal["locations"]) > 0:
        output.append(f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n')

    if "type" in characteristics:
        output.append(f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n')

    output.append('  </p>\n')
    output.append('</li>\n')

    return "".join(output)


def serialize_animals(animals_data):
    """Converts a list of animal objects into HTML"""
    output = []

    for animal in animals_data:
        output.append(serialize_animal(animal))

    return "".join(output)


def write_html_to_file(template_file, output_file, placeholder, replacement):
    """Reads an HTML template, replaces the placeholder and writes the final HTML file"""
    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace(placeholder, replacement)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    animals_data = load_data(DATA_FILE)
    animals_html = serialize_animals(animals_data)
    write_html_to_file(TEMPLATE_FILE, OUTPUT_FILE, PLACEHOLDER, animals_html)


if __name__ == "__main__":
    main()