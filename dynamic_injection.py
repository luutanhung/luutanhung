import os
import time
import glob

import requests

TEMPLATE_FILE = "README.template.md"
OUTPUT_FILE = "README.md"


def dynamic_inject():
    url: str = "https://finance-quote-api.onrender.com/api/quotes/random?quote_type=inspiration&response_type=svg&theme=light"
    response = requests.get(url)

    if response.status_code == 200:
        for file in glob.glob("./assets/*.svg"):
            os.remove(file)

        filename: str = f"quote-{int(time.time())}.svg"
        with open(f"./assets/{filename}", "w", encoding="utf-8") as f:
            f.write(response.text)

        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            template = f.read()

        readme_content = template.replace(
            "{finance_quote_svg}", f"![Finance Quote](/assets/{filename})"
        )

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(readme_content)

        print("README.md updated with a new Finance Quote.")


if __name__ == "__main__":
    dynamic_inject()
