import os
import shutil
from pathlib import Path


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


######## Remove Template Files for Website ##########
path = Path(os.getcwd())
parent_path = path.parent.absolute()
cookiecutter_var = "{{cookiecutter.use_website_template}}"
remove_templates = cookiecutter_var == "no"

if remove_templates:
    for folder in ["css", "images", "js", "webfonts"]:
        folder_path = os.path.join(
            parent_path, "{{cookiecutter.project_slug}}", "app", "static", f"{folder}"
        )
        remove(folder_path)

    for html_template in ["elements.html", "generic.html", "LICENSE.txt"]:
        folder_path = os.path.join(
            parent_path,
            "{{cookiecutter.project_slug}}",
            "app",
            "templates",
            f"{html_template}",
        )
        remove(folder_path)
######################################################
