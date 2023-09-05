'''Infra for creating recursively linked graphs of dataclass-like objects.

dataclass & friends are great for capturing properties of data, including
hierarchical data.

However, hierarchies of dataclass objects are limited in that:
    1) they don't provide any parent pointers.
    2) they don't easily allow references to other objects (foreign keys)
    3) they don't make it easy to pretty-print objects in-context.

This module provides a layer on-top of dataclasses to address these limitations.

some limitations of the code in this module:
    1) all nodes in the graph must be frozen.
'''


import dataclasses as dc


class graphnode:
    def __init__(self, cls):
        self.cls = dc.dataclass(cls, repr=False, frozen=True, kw_only=True)

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)


if __name__ == '__main__':
    @graphnode
    class TestClass:
        foo: str

    x = TestClass(foo='a')
    print(x.foo)
