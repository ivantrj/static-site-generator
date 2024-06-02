from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images,extract_markdown_links

# The main function of the script
def main():
  text = TextNode("This is a text node", "bold", "https://www.google.com")
  print(text)


main()