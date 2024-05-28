from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

# The main function of the script
def main():
  text = TextNode("This is a text node", "bold", "https://www.google.com")
  print(text)

  htmlnode = HTMLNode("div", None, [text], {"href": "https://www.google.com", "target": "_blank"})
  print(htmlnode.props_to_html())

  leafnode = LeafNode("a", "Click me!", {}, {"href": "https://www.google.com"})
  print(leafnode.to_html())



main()
