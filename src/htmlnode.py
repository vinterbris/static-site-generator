

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