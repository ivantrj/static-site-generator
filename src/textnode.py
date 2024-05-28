class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        self.text - The text content of the node
        self.text_type - The type of text this node contains, which is just a string like "bold" or "italic"
        self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"