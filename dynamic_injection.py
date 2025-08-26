import requests

TEMPLATE_FILE = "README.template.md"
OUTPUT_FILE = "README.md"


def dynamic_inject():
    url = "https://officeapi.akashrajpurohit.com/quote/random"
    response = requests.get(url)
    data = response.json()

    quote = data.get("quote", "No quote found!")
    character = data.get("character", "Unknown")

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    readme_content = template.replace("{office_quote}", quote).replace(
        "{office_character}", character
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md updated with new quote.")


if __name__ == "__main__":
    dynamic_inject()
