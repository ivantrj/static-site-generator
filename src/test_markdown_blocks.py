import unittest
from markdown_blocks import (
  markdown_to_blocks,
)

def test_markdown_to_blocks(self):
  blocks = markdown_to_blocks("This is a text node\n\nThis is another text node")
  self.assertListEqual(["This is a text node", "This is another text node"], blocks)