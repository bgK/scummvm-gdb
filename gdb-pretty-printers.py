__license__ = 'GPLv2+'

class CommonStringPrinter:
    """Print a Common::String"""

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return self.val['_str'].string()

    @staticmethod
    def display_hint():
        return 'string'

class CommonArrayPrinter:
    """Print a Common::Array"""

    class _Iterator:
        def __init__(self, storage, size):
            self.item = storage
            self.size = size
            self.count = 0

        def __iter__(self):
            return self

        def __next__(self):
            count = self.count
            self.count += 1
            if self.count > self.size:
                raise StopIteration
            elt = self.item.dereference()
            self.item += 1
            return '[%d]' % count, elt

    def __init__(self, val):
        self.val = val

    def children(self):
        return self._Iterator(self.val['_storage'],
                              self.val['_size'])

    def to_string(self):
        return ('%s of size %d, capacity %d'
                % (self.val.type.name, self.val['_size'], self.val['_capacity']))

    @staticmethod
    def display_hint():
        return 'array'

class MathVector3dPrinter:
    """Print a Math::Vector3d"""

    class _Iterator:
        def __init__(self, storage):
            self.item = storage
            self.size = 3
            self.count = 0
            self.names = ('x', 'y', 'z')

        def __iter__(self):
            return self

        def __next__(self):
            count = self.count
            self.count += 1
            if self.count > self.size:
                raise StopIteration

            return '[%s]' % self.names[count], self.item[count]

    def __init__(self, val):
        self.val = val

    def children(self):
        return self._Iterator(self.val['_values'])

    @staticmethod
    def display_hint():
        return 'array'

printers = gdb.printing.RegexpCollectionPrettyPrinter('scummvm')
printers.add_printer('Common::String', '^Common::String$', CommonStringPrinter)
printers.add_printer('Common::Array', '^Common::Array<.*>$', CommonArrayPrinter)
printers.add_printer('Math::Vector3d', '^Math::Matrix<3, 1>$', MathVector3dPrinter)
gdb.printing.register_pretty_printer(None, printers, True)

