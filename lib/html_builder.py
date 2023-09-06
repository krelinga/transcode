'''HTML building & manipulation utilities.'''


from html import escape


class Attributes:
    def __init__(self):
        self._attrs = []

    def __call__(self, key, value):
        self._attrs.append((key, value))

    def Render(self) -> str:
        leading_space = ' ' if len(self._attrs) > 0 else ''
        return (
                leading_space +
                ' '.join([f'{escape(x[0])}="{escape(x[1])}"' for x in self._attrs]))


class _BaseTag:
    def __init__(self, name):
        self._name = name
        self._attr = Attributes()

    @property
    def name(self):
        return self._name

    @property
    def attr(self):
        return self._attr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


class Text:
    def __init__(self, text):
        self._text = text

    def Render(self) -> str:
        return escape(self._text)


class OpenAndCloseTag(_BaseTag):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def text(self, text):
        self._children.append(Text(text))

    def tag(self, tag: _BaseTag):
        self._children.append(tag)
        return tag

    def Render(self) -> str:
        return ''.join([
            f'<{escape(self.name)}',
            f'{self.attr.Render()}>',
            ' '.join([x.Render() for x in self._children]),
            f'</{escape(self.name)}>'])


class SelfClosingTag(_BaseTag):
    def Render(self) -> str:
        return f'<{escape(self.name)}{self.attr.Render()} />'


class OpenOnlyTag(_BaseTag):
    def Render(self) -> str:
        return f'<{escape(self.name)}{self.attr.Render()}>'


def html(): return OpenAndCloseTag('html')

def img(): return SelfClosingTag('img')

def input(): return OpenOnlyTag('input')


if __name__ == '__main__':
    attrs = Attributes()
    attrs('foo', 'bar>')
    attrs('<baz', '"biff"')
    print(attrs.Render())
    print(len(Attributes().Render()))

    print(html().Render())
    with html() as root:
        root.attr('foo', 'bar')
        root.attr('class', 'someclass')
        root.text('test text')
        with root.tag(img()) as test_img:
            test_img.attr('src', 'test_src')
        print(root.Render())

    with img() as tag:
        tag.attr('src', '/path/to/image.jpg')
        tag.attr('alt', 'Some Description')
        print(tag.Render())

    with input() as tag:
        tag.attr('a', 'b')
        tag.attr('c', 'd')
        print(tag.Render())
