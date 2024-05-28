from textnode import TextNode
from htmlnode import HTMLNode

# The main function of the script
def main():
  text = TextNode("This is a text node", "bold", "https://www.google.com")
  print(text)

  htmlnode = HTMLNode("div", None, [text], {"href": "https://www.google.com", "target": "_blank"})
  print(htmlnode)

  print(htmlnode.props_to_html())


main()
