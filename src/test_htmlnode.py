import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        with self.assertRaises(ValueError):
            node = LeafNode(
                value='',
                tag="div",
                props={"class": "greeting", "href": "https://boot.dev"},
            )
            node.to_html()


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

class TestParentNode(unittest.TestCase):
    def test_with_leaf_children(self):
        node = ParentNode(
            'p',
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_with_props(self):
        node = ParentNode(
            'p',
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
            props={"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.to_html(),
            '<p class="greeting" href="https://boot.dev"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_with_parents_and_children(self):
        node = ParentNode(
            'p',
            [
                ParentNode(
                    'p',
                    [
                        LeafNode("Bold text", "b"),
                        LeafNode("Normal text", None),
                        LeafNode("italic text", "i"),
                        LeafNode("Normal text", None),
                    ],
                ),
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text", "i"),
                LeafNode("Normal text", None),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag="",
                children= [
                    LeafNode("Bold text", "b")
                ],
                value='hello',
                props={"class": "greeting", "href": "https://boot.dev"},
            )
            node.to_html()


    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                tag="p",
                children=[],
                value='hello',
                props={"class": "greeting", "href": "https://boot.dev"},
            )
            node.to_html()

if __name__ == "__main__":
    unittest.main()