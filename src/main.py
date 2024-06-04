
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
  html_content = markdown_to_html_node(markdown).to_html()
  print(f"Html content: {html_content}")

  html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

  with open(dest_path, "w") as f:
    f.write(html)

import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  for filename in os.listdir(dir_path_content):
      from_path = os.path.join(dir_path_content, filename)
      
      if filename.endswith(".md"):
          print(f"Processing markdown file: {from_path}")
          dest_path = os.path.join(dest_dir_path, filename.replace(".md", ".html"))
          generate_page(from_path, template_path, dest_path)
      elif os.path.isdir(from_path):
          print(f"Entering directory: {from_path}")
          dest_subdir = os.path.join(dest_dir_path, filename)
          if not os.path.exists(dest_subdir):
              os.makedirs(dest_subdir)
          generate_pages_recursive(from_path, template_path, dest_subdir)



def main():

  generate_pages_recursive("./content", "template.html", dir_path_public)



main()