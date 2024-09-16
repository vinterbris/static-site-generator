

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

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == self.props

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('all leaf nodes should have value')
        if self.tag is None:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None, value=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('tag is required')
        if not self.children:
            raise ValueError('children are required')
        children = ''
        for child in self.children:
            children += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'

