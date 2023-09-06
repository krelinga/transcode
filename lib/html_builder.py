'''HTML building & manipulation utilities.'''


from collections import abc
from html import escape


class Attrs:
    def __init__(self, **kwargs):
        self._attrs = kwargs


class _BaseTag:
    def __init__(self, name, *children):
        self._name = name
        self._children = children

    def _RenderAttrs(self) -> str:
        attr_wrappers = list(filter(lambda x: type(x) == Attrs, self._children))
        assert len(attr_wrappers) <= 1
        entries = []
        for attr_wrapper in attr_wrappers:
            for attr, value in attr_wrapper._attrs.items():
                entries.append(f' {escape(attr)}="{escape(value)}"')
        return ''.join(entries)


class OpenAndCloseTag(_BaseTag):
    def Render(self) -> str:
        def render_child(child):
            if isinstance(child, _BaseTag):
                return child.Render()
            elif isinstance(child, abc.Iterable) and type(child) != str:
                return ' '.join([render_child(x) for x in child])
            else:
                return escape(f'{child}')

        return ''.join([
            f'<{escape(self._name)}',
            f'{self._RenderAttrs()}>',
            ' '.join([
                render_child(x)
                for x in filter(lambda x: type(x) != Attrs, self._children)]),
            f'</{escape(self._name)}>'])


class SelfClosingTag(_BaseTag):
    def Render(self) -> str:
        return f'<{escape(self._name)}{self._RenderAttrs()} />'


class OpenOnlyTag(_BaseTag):
    def Render(self) -> str:
        return f'<{escape(self._name)}{self._RenderAttrs()}>'


def body(*args): return OpenAndCloseTag('body', *args)
def head(*args): return OpenAndCloseTag('head', *args)
def html(*args): return OpenAndCloseTag('html', *args)
def h1(*args): return OpenAndCloseTag('h1', *args)
def h3(*args): return OpenAndCloseTag('h3', *args)
def img(*args): return SelfClosingTag('img', *args)
def input(*args): return OpenOnlyTag('input', *args)
def li(*args): return OpenAndCloseTag('li', *args)
def p(*args): return OpenAndCloseTag('p', *args)
def pre(*args): return OpenAndCloseTag('pre', *args)
def table(*args): return OpenAndCloseTag('table', *args)
def td(*args): return OpenAndCloseTag('td', *args)
def th(*args): return OpenAndCloseTag('th', *args)
def title(*args): return OpenAndCloseTag('title', *args)
def tr(*args): return OpenAndCloseTag('tr', *args)
def ul(*args): return OpenAndCloseTag('ul', *args)


if __name__ == '__main__':
    print(html().Render())
    print(html(
        Attrs(**{'foo': 'bar', 'class': 'someclass'}),
        'test text', img(Attrs(src='test_src'))).Render())

    print(img(Attrs(src='/path/to/image.jpg')).Render())

    print(input(Attrs(a='b', c='d')).Render())
