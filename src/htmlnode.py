

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented('to_html method not implemented')

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = []
        for k, v in self.props.items():
            attributes.append(f'{k}="{v}"')
        return ' ' + ' '.join(attributes)

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props=props, children=None)

    def to_html(self):
        print(self.value, self.tag, self.props)
        if not self.value:
            raise ValueError('all leaf nodes should have value')
        if self.tag is None:
            return self.value
        if self.props is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        return f'<{self.tag}>{self.value}</{self.tag}>'

node = LeafNode(
            "Hello, world!",
            "div",
            {"class": "greeting", "href": "https://boot.dev"},
        )
print(node)