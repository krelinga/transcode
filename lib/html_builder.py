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
            if type(child) == type(''):
                return escape(child)
            elif isinstance(child, abc.Iterable):
                return ' '.join([render_child(x) for x in child])
            else:
                return child.Render()

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


def body(*args, **kwargs): return OpenAndCloseTag('body', *args, **kwargs)
def head(*args, **kwargs): return OpenAndCloseTag('head', *args, **kwargs)
def html(*args, **kwargs): return OpenAndCloseTag('html', *args, **kwargs)
def h1(*args, **kwargs): return OpenAndCloseTag('h1', *args, **kwargs)
def img(*args, **kwargs): return SelfClosingTag('img', *args, **kwargs)
def input(*args, **kwargs): return OpenOnlyTag('input', *args, **kwargs)
def li(*args, **kwargs): return OpenAndCloseTag('li', *args, **kwargs)
def p(*args, **kwargs): return OpenAndCloseTag('p', *args, **kwargs)
def title(*args, **kwargs): return OpenAndCloseTag('title', *args, **kwargs)
def ul(*args, **kwargs): return OpenAndCloseTag('ul', *args, **kwargs)


if __name__ == '__main__':
    print(html().Render())
    print(html(
        Attrs(**{'foo': 'bar', 'class': 'someclass'}),
        'test text', img(Attrs(src='test_src'))).Render())

    print(img(Attrs(src='/path/to/image.jpg')).Render())

    print(input(Attrs(a='b', c='d')).Render())
