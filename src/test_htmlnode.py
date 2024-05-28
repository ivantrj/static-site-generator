import unittest
from htmlnode import HTMLNode, LeafNode

class TestPropsToHTML(unittest.TestCase):

    def test_empty_props(self):
        node = HTMLNode('div', None, [], {})
        self.assertEqual(node.props_to_html(), '')

    def test_single_prop(self):
        node = HTMLNode('div', None, [], {'id': 'my-div'})
        self.assertEqual(node.props_to_html(), 'id="my-div"')

    def test_multiple_props(self):
        node = HTMLNode('div', None, [], {'id': 'my-div', 'class': 'my-class'})
        self.assertEqual(node.props_to_html(), 'id="my-div" class="my-class"')

    def test_prop_values_with_spaces(self):
        node = HTMLNode('div', None, [], {'data-tooltip': 'This is a tooltip with spaces'})
        self.assertEqual(node.props_to_html(), 'data-tooltip="This is a tooltip with spaces"')

if __name__ == "__main__":
    unittest.main()


class TestLeafNode(unittest.TestCase):
  def test_to_html_none_value(self):
    node = LeafNode('div', None, [], {})
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_empty_tag(self):
    node = LeafNode('', 'hello', [], {})
    self.assertEqual(node.to_html(), 'hello')

  def test_to_html_with_tag(self):
    node = LeafNode('h1', 'hello', [], {'id': 'my-heading'})
    self.assertEqual(node.to_html(), '<h1 id="my-heading">hello</h1>')

if __name__ == "__main__":
    unittest.main()