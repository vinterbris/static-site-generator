from src.htmlnode import LeafNode
from src.textnode import TextNode


def text_node_to_html_node(text_node: TextNode) :
    if text_node.text_type == 'text':
        return LeafNode(text_node.text)
    if text_node.text_type == 'bold':
        return LeafNode(text_node.text, tag='b')
    if text_node.text_type == 'italic':
        return LeafNode(text_node.text, tag='i')
    if text_node.text_type == 'code':
        return LeafNode(text_node.text, tag='code')
    if text_node.text_type == 'link':
        return LeafNode(text_node.text, tag='a', props={"href": text_node.url})
    if text_node.text_type == 'image':
        return LeafNode('', tag='img', props={"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception('Incorrect text_type')

def split_nodes_delimiter(old_nodes, delimiter, text_type):
