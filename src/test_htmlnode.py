import unittest
from htmlnode import HTMLNode

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