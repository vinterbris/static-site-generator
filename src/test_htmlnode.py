import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode(
            value='',
            tag="div",
            props={"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertRaises(ValueError)

    def test_no_tag(self):
        node = LeafNode(
            value='Hello, world!',
            tag=None,
            props={"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            'Hello, world!'
        )

    def test_to_html_with_props(self):
        node = LeafNode(
            "Hello, world!",
            "div",
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" href="https://boot.dev">Hello, world!</div>',
        )

    def test_to_html_without_props(self):
        node = LeafNode(
            "Hello, world!",
            "div",
        )
        self.assertEqual(
            node.to_html(),
            '<div>Hello, world!</div>',
        )


if __name__ == "__main__":
    unittest.main()