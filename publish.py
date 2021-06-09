import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent


def render_page(environment, directory, page):
    if not environment or not page:
        return

    template = environment.get_template(page)
    output = template.render()

    with open(directory / page, "w+") as f:
        f.write(output)


def main():
    pages_dir = BASE_DIR / "pages"
    rendered_dir = BASE_DIR / "public"

    if not pages_dir.is_dir():
        print("pages must be a directory")
        sys.exit(1)

    if not rendered_dir.exists():
        rendered_dir.mkdir()

    jinja2_env = Environment(
        loader=FileSystemLoader(searchpath=pages_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    for page in pages_dir.iterdir():
        if page.name.endswith(".html"):
            render_page(jinja2_env, rendered_dir, page.name)


if __name__ == "__main__":
    main()
