
import shutil
import os

from copystatic import copy_files_recursive
from markdown_blocks import markdown_to_html_node
from htmlnode import ParentNode

dir_path_static = "./static"
dir_path_public = "./public"

def extract_title(markdown):
  if markdown.startswith("# "):
    return markdown[2:]
  else:
    raise Exception("No header")

def generate_page(from_path, template_path, dest_path):
  print("Generating page from " + from_path + " to " + dest_path)

  with open(from_path, "r") as f:
    markdown = f.read()

  with open(template_path, "r") as f:
    template = f.read()

  title = extract_title(markdown)
  html = markdown_to_html_node(markdown).to_html()

  html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

  with open(dest_path, "w") as f:
    f.write(html)

def copy_files():
  generate_page("content/index.md", "./template.html", dir_path_public + "/index.html")

def main():

  copy_files()



main()