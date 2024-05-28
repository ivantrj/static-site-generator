import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(text='This is a text node', text_type='bold', url=None)")

    def test_str(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(str(node), "This is a text node")

    def test_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")


if __name__ == "__main__":
    unittest.main()
