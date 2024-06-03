from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

# The main function of the script
def main():
  text = TextNode("This is a text node", "bold", "https://www.google.com")
  print(text)

  print(text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"))



main()