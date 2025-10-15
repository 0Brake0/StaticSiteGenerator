import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links 
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_simple(self):
        node = TextNode("x `y` z", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        # assert the 3 nodes with correct types/texts

    def test_bold_multiple(self):
        node = TextNode("a **b** c **d**", TextType.TEXT)
        out = split_nodes_delimiter([node], "**", TextType.BOLD)
        # assertions

    def test_unmatched_raises(self):
        node = TextNode("a **b", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

if __name__ == "__main__":
    unittest.main()