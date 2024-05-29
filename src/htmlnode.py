class HTMLNode():
  def __init__(self, tag, value, children, props):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    if self.props is None:
        return ""
    props_html = ""
    return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

  def __repr__(self):
    return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"


# TODO: Make value required
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("Invalid HTML: no value")
    if self.tag is None:
      return self.value
    else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
  def __init__(self, tag, children):
    self.tag = tag
    self.children = children
    # self.props = props

  def to_html(self):
    if self.tag is None:
      raise ValueError("Invalid HTML: no value")
    if self.children is None:
      raise ValueError("Invalid HTML: no children")
  
    children_html = ''
    for child in self.children:
      children_html += child.to_html()

    return f"<{self.tag}>{children_html}</{self.tag}>"

