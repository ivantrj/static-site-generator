class HTMLNode():
  def __init__(self, tag, value, children, props):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

  def __repr__(self):
    return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, children, props):
    super().__init__(tag, value, children, props)

  def to_html(self):
    if self.value is None:
      raise ValueError
    elif self.tag == "":
      return self.value
    else:
      return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
