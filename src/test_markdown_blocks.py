import unittest
from markdown_blocks import (
  markdown_to_blocks,
  block_to_block_type,
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_ordered_list,
  block_type_unordered_list,
  block_type_quote,
)


class TestMarkdownToHTML(unittest.TestCase):
  def test_markdown_to_blocks(self):
    blocks = markdown_to_blocks("This is a text node\n\nThis is another text node")
    self.assertListEqual(["This is a text node", "This is another text node"], blocks)

  def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)