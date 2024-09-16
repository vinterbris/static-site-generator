import unittest

from src.utils.converters import text_node_to_html_node
from src.htmlnode import LeafNode
from src.textnode import TextNode


class test_text_node_to_html_node(unittest.TestCase):
    def test_text(self):
        txt_node = TextNode('hello', 'text')
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, None)

    def test_bold(self):
        txt_node = TextNode('hello', 'bold')
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, None)

    def test_italic(self):
        txt_node = TextNode('hello', 'code')
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, None)

    def test_code(self):
        txt_node = TextNode('hello', 'code')
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, None)

    def test_link(self):
        url = 'boot.dev'

        txt_node = TextNode('hello', 'link', url)
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "hello")
        self.assertEqual(html_node.props, {"href": url})

    def test_image(self):
        url = 'boot.dev'
        text = 'hello'

        txt_node = TextNode(text, 'image', url)
        html_node = text_node_to_html_node(txt_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": url, "alt": text})

    def test_incorrect_type(self):
        with self.assertRaises(Exception):
            txt_node = TextNode('hello', 'node')
            html_node = text_node_to_html_node(txt_node)