from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        html_parts = []
        for k, v in self.props.items():
            html_parts.append(f' {k}="{v}"')
        return " " + " ".join(html_parts)

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
        )

    def __repr__(self):
        return f"HTMLNode ({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have value!")
        if self.tag is None:
            return f"{self.value}"
        attrs = self.props_to_html()
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires tag!")
        if not self.children:
            raise ValueError("ParentNode requires children")
        attrs = self.props_to_html()
        child_str = ""
        for child in self.children:
            child_str += child.to_html()
        return f"<{self.tag}{attrs}>{child_str}</{self.tag}>"
